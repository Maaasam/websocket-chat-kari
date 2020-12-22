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
#NGワードを受け取る
ngword = sys.stdin.readline()
ngword = ngword.replace('\n','')
#チャットに打ち込まれたメッセージを受け取る
data = sys.stdin.readline()
data = data.replace('\n' , '')
#print(ngword)
#print(data)
#print("----------------")
#########################################

#########################################
#word2vecの学習済みモデルを呼び出す
#Herokuにあげるとき、modelの場所注意、パスをちゃんと通すこと
model = gensim.models.KeyedVectors.load_word2vec_format('./data/jawiki.word_vectors.200d.100000.bin', binary=True)


try:
    word_0 = data
    results = model.wv.most_similar(word_0)
    
    word_1 = data
    word_2 = ngword
    
    a = model.wv.__getitem__(word_1)
    b = model.wv.__getitem__(word_2)
    cos_sim = np.dot(a, b)/np.linalg.norm(a)/np.linalg.norm(b)
    #if con_sim > 0.65:
    print(cos_sim)
    
except KeyError as error:
    err = 0
    print(err)

#########################################

ngword = ''
data = ''
