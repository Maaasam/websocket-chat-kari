#!/usr/bin/env python
# coding: utf-8

#word2vecをインポート
from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt
import gensim

#w2v_node.jsから値をひろう
import sys

#MeCabをインポート
import MeCab
import re

#########################################
#形態素解析したい文章 .jsから引っ張ってくる
#チャットに打ち込まれたメッセージを受け取る
data = sys.stdin.readline()
data = data.replace('\n' , '')
#########################################

#########################################
mecab = MeCab.Tagger("-Ochasen")
#MeCabを呼び出す(Taggerの引数は辞書の指定)
#改行ごとに文章を分割

node = mecab.parseToNode(data)
#名詞だけ抜き出す
meisi=[]
while node:
    word = node.surface
    hinshi = node.feature.split(",")[0]
    if (hinshi == "名詞"):
        #名詞を取り出す
        meisi.append(word)
        print(word)
    else:
        print(-1)
    node = node.next

#("名詞 ： {}".format(meisi))
#print("-------------")
#########################################

