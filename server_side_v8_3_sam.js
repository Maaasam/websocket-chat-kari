//front_page_v1_2.htmlと連動
// S01. 必要なモジュールを読み込む
var http = require('http');
var socketio = require('socket.io');
var fs = require('fs');

//.pyファイルを呼び出す
var {PythonShell} = require('python-shell');

var path = require('path');
var mime = {
    '.html': 'text/html',
    '.css': 'text/css',
};

// S02. HTTPサーバを生成する
var server = http.createServer(function(req, res) {
    console.log(req.url);
    var filePath = '';
    if(req.url == '/' || req.url == '/?') {
        filePath = '/front_page_v8_3_sam.html';
    } else if(req.url == '/clear') {
        filePath = '/finish_page8_3_sam.html';
    } else if(req.url == '/reclear'){
        filePath = '/front_page_v8_3_sam.html';
    }else {
        filePath = req.url;
    }
    if(req.url != '/favicon.ico') {
        var fullPath = __dirname + filePath;
        res.writeHead(200, {'Content-Type' : mime[path.extname(fullPath)] || 'text/plain'});
        res.end(fs.readFileSync(fullPath, 'utf-8'));
    } else {
    }
}).listen(process.env.PORT || 5000);  // ポート競合の場合は値を変更

// S03. HTTPサーバにソケットをひも付ける（WebSocket有効化）
var io = socketio.listen(server);
console.log(process.env.PORT);

console.log("Connection");

// S04. connectionイベント・データを受信する
//双方向のイベントをおこすとこ
io.sockets.on('connection', function(socket) {
    var name;
    //var box=[];
    var check_list =['ジャガイモ','トウモロコシ','大豆','サトウキビ','トマト','ニンジン','ブドウ','バナナ','パイナップル','イチゴ','メロン','リンゴ','寿司','ラーメン','焼肉','パスタ','スープ','カレー','ジェットコースター','タクシー','観覧車','自動車','猫','犬','ウサギ','オオカミ','キツネ','ネズミ','旅館','リゾートホテル','レストラン','ショッピングセンター','大学','たまねぎ','アミューズメント'];
    
    ///////ランダム作成
    var min = 0;
    var max = 49;
    var random_number = 0;
    var word = '';
    var groupid = 0;
    let group = [];
    ///////
    
    // S05. client_to_serverイベント・データを受信する
    socket.on('client_to_server', function(data) {
        // S06. server_to_clientイベント・データを送信する
        io.sockets.emit('server_to_client', data);
        
    });
    // S07. client_to_server_broadcastイベント・データを受信し、送信元以外に送信する
    socket.on('client_to_server_broadcast', function(data) {
        socket.broadcast.emit('start_server_to_client', {value : data.value});
    });
    // S08. client_to_server_personalイベント・データを受信し、送信元のみに送信する
    socket.on('client_to_server_personal', function(data) {
        var id = socket.id;
        name = data.value;
        var personalMessage = "あなたは、" + name + "さんとして入室しました。"
        io.to(id).emit('start_server_to_client', {value : personalMessage});
    });
    // S09. disconnectイベントを受信し、退出メッセージを送信する
    socket.on('disconnect', function() {
        if (name == 'undefined') {
            console.log("未入室のまま、どこかへ去っていきました。");
        } else {
            var endMessage = name + "さんが退出しました。"
            socket.broadcast.emit('server_to_client', {value : endMessage});
        }
    });
    
    ////////////NGワード配布
    socket.on('distribute_word',function(data){
        console.log("Distribute Word Server");
        
        var id = socket.id;
        name = data.value;
        
        //NGワード取得
        var ngword = choose_at_random(check_list);
        var ong_sentence="[ " + name + " ]さん：" + "【 " +　ngword + " 】";
        console.log(ong_sentence);
        
        //.pyファイルを呼び出す
        var pyshell_mec = new PythonShell('game_ngword_sam.py');
        
        pyshell_mec.send(ngword);
        
        pyshell_mec.on('message', function(data){
            group = data;
            console.log("group : " + group);
            io.to(id).emit('ngword_save',{word:ngword, group:group});//送信元のみ
        });
        
    });
    function choose_at_random(arrayData) {
        //var i = arrayData.length-1;
        var arrayIndex = Math.floor(Math.random() * arrayData.length);
        //i=i-1;
        //arrayIndexが場所に当たるからid_num[arrayIndex]=id;
        return arrayData[arrayIndex];
    }
    
    //途中から入ったときに他プレイヤのNGワードをもらう
    socket.on('1',function(data){
        console.log("1入った");
        var id = socket.id;
        socket.broadcast.emit('2', {value : id});
        
        io.to(id).emit('5',{});
    });
    socket.on('3',function(data){
        var my_id = data.value;
        var other_id = socket.id;
        var other_name = data.name;
        var other_ngword = data.word;
        console.log("3入った" + my_id + other_ngword);
        if(other_name != ""){
            io.to(my_id).emit('4',{id : other_id, name : other_name, value : other_ngword});
        }
    });
    socket.on('6',function(data){
        console.log("6入った");
        var my_id = socket.id;
        var my_name = data.name;
        var my_ngword = data.word;
        var ong_sentence="[ " + my_name + " ]さん：" + "【 " +　my_ngword + " 】";
        socket.broadcast.emit('ngword_display',{id : my_id, value : ong_sentence});
    });
    ////////////
    
    ////////////形態素解析・word2vec
    socket.on('mecab_one',function(data){
        var id = socket.id;
        var name = data.name;
        var ngword = data.word;
        var group = data.group;
        var message = data.message;
        var meisi = [];
        
        //.pyファイルを呼び出す
        var pyshell_mec = new PythonShell('game_mec_sam.py');
        
        pyshell_mec.send(message);
        
        pyshell_mec.on('message', function(data){
            if(data != -1){
                console.log("mecでのgroup : " + group);
                var result = group.indexOf(data);
                console.log("mecでのresult" + result);
                if(result != -1){
                    //減点
                    console.log("減点");
                    io.sockets.emit('ng_deduction',{value : data});
                }
                if(result == -1){
                    meisi.push(data);
                    console.log("pyへ送る：" + data + ngword);
                    //.pyファイルを呼び出す
                    var pyshell_w2v = new PythonShell('game_w2v_sam.py');
                    
                    pyshell_w2v.send(ngword);
                    pyshell_w2v.send(data);
                    
                    pyshell_w2v.on('message', function(data){
                        console.log(data + "と" + ngword + "との類似度：" + data);
                        io.to(id).emit('groupMessage_two',{value : data});
                    });
                }
            }
        });
        
    });
    
    socket.on('gayainfo', function(data) {
        // ガヤの結果を送信する
        io.sockets.emit('gayainfoDid', data);
        
    });
    ////////////
    
    ////////////OKワード記入
    ////////////
    
    ////////////チャレンジボタン NGワードを当てる
    //メッセージと結果を全員に送る
    socket.on('challenge_btn_click',function(data){
        console.log("challenge_btn_click_button");
        io.sockets.emit('challenge_message', data);
    });
    socket.on('challenge_btn_result',function(data){
        io.sockets.emit('challenge_result',{value : data.value});
    });
    ////////////
    
    ////////////アタックボタン 特定の誰かのPOINTワードを当てる
    socket.on('attack_btn_click',function(data){//例 date =「aさんのAワード」
        console.log(data.name + "さんがアタック：" + data.message);
        io.sockets.emit('attack_check',data);
    });
    
    socket.on('attack_result',function(data){
       io.sockets.emit('attack_result_send',data);
    });
    ////////////
    
    ////////////チェンジボタン　NG・POINTワードを変更
    socket.on('word_change',function(){
        var id = socket.id;
        
        //NGワード
        var ngword = choose_at_random(check_list);
        var ong_sentence ="チェンジ ▶︎ [ " + name + " ]さん：" + "【 " + ngword + " 】";
        console.log(ong_sentence);
        
        //.pyファイルを呼び出す
        var pyshell_mec = new PythonShell('game_ngword_sam.py');
        
        pyshell_mec.send(ngword);
        
        pyshell_mec.on('message', function(data){
            group = data;
            console.log("group : " + group);
            io.to(id).emit('ngword_save',{word:ngword, group:group});//送信元のみ
        });
        
        socket.broadcast.emit('ngword_display',{value : ong_sentence});//送信元以外
        
        //POINTワード
        var start = 1;
        io.to(id).emit('pointword_change',{value:start});
    });
    ////////////
    
    
    var alert_message = '';
    ////////////アラート
    socket.on('client_to_server_alert',function(data){
        console.log("2"+ data.value);
        //io.sockets.emit('server_to_client_alert', {value : data.value});
        
        alert_message = data.value;
        console.log("alert_message : " + alert_message);
    });
    ////////////
    
    
    ///////  finish_page2.html  //////////////////////////
    ////////////
    socket.on('client_to_server_result',function(data){
        console.log("client_to_server_result");
        io.sokets.emit('server_to_client_result',{value:alert_message});
    });
    ////////////
    
});
