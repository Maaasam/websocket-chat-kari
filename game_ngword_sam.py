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
#NGワードを受け取る
ngword = sys.stdin.readline()
ngword = ngword.replace('\n','')
#########################################

"""
['ジャガイモ','トウモロコシ','大豆','サトウキビ','トマト','ニンジン','たまねぎ',
 'ブドウ','バナナ','パイナップル','イチゴ','メロン','リンゴ',
 '寿司','ラーメン','焼肉','パスタ','スープ','カレー',
 'ジェットコースター','タクシー','観覧車','自動車',
 '猫','犬','ウサギ','オオカミ','キツネ','ネズミ',
 '旅館','リゾートホテル','レストラン','ショッピングセンター','大学','アミューズメント']

apple = ['りんご','リンゴ','林檎','アップル']
strawberry = ['いちご','イチゴ','苺','ストロベリー']
orange= ['みかん','ミカン','蜜柑']
grape = ['ぶどう','ブドウ','葡萄','グレープ']
melon = ['メロン','めろん']
cherry = ['さくらんぼ','サクランボ','チェリー']
persimmon = ['柿','かき','カキ']
"""
vegatable_1 = ['ジャガイモ','じゃがいも','ポテト']
vegatable_2 = ['トウモロコシ','とうもろこし','コーン']
vegatable_3 = ['大豆','だいず','ソイ','soy']
vegatable_4 = ['サトウキビ','さとうきび','砂糖きび']
vegatable_5 = ['トマト','とまと','トメト','tomato']
vegatable_6 = ['ニンジン','にんじん','キャロット','carrot']
vegatable_7 = ['たまねぎ','タマネギ','玉ねぎ','玉葱','オニオン']
fruit_1 = ['ブドウ','ぶどう','葡萄','グレープ']
fruit_2 = ['バナナ','ばなな','banana']
fruit_3 = ['パイナップル','ぱいなっぷる','pineapple']
fruit_4 = ['イチゴ','いちご','苺','ストロベリー']
fruit_5 = ['メロン','めろん','melon']
fruit_6 = ['リンゴ','りんご','林檎','アップル','apple']
food_1 = ['寿司','すし','shusi','鮨']
food_2 = ['ラーメン','らーめん']
food_3 = ['焼肉','やきにく','焼き肉','やき肉']
food_4 = ['パスタ','ぱすた','pasta']
food_5 = ['スープ','すーぷ','soup']
food_6 = ['カレー','かれー','curry']
vehicle_1 = ['ジェットコースター','じぇっとこーすたー']
vehicle_2 = ['タクシー','たくしー','taxi']
vehicle_3 = ['観覧車','かんらんしゃ','カンランシャ']
vehicle_4 = ['自動車','じどうしゃ','車','car']
animal_1 = ['猫','cat','ねこ','ネコ']
animal_2 = ['犬','いぬ','イヌ','dog']
animal_3 = ['ウサギ','うさぎ','兎','ラビット']
animal_4 = ['オオカミ','狼','おおかみ','ウルフ']
animal_5 = ['キツネ','きつね','fox','狐']
animal_6 = ['ネズミ','ねずみ','鼠','マウス']
building_1 = ['旅館','りょかん','リョカン']
building_2 = ['リゾートホテル','りぞーとほてる']
building_3 = ['レストラン','れすとらん','restaurant']
building_4 = ['ショッピングセンター','しょっぴんぐせんたー']
building_5 = ['大学','学校','だいがく','カレッジ','ユニバーシティ']
building_6 = ['アミューズメント','あみゅーずめんと']


result = ngword in vegatable_1
if(result == True):
    group = vegatable_1
    print(vegatable_1)
result = ngword in vegatable_2
if(result == True):
    group = vegatable_2
    print(vegatable_2)
result = ngword in vegatable_3
if(result == True):
    group = vegatable_3
    print(vegatable_3)
result = ngword in vegatable_4
if(result == True):
    group = vegatable_4
    print(vegatable_4)
result = ngword in vegatable_5
if(result == True):
    group = vegatable_5
    print(vegatable_5)
result = ngword in vegatable_6
if(result == True):
    group = vegatable_6
    print(vegatable_6)
result = ngword in vegatable_7
if(result == True):
    group = vegatable_7
    print(vegatable_7)

result = ngword in fruit_1
if(result == True):
    group = fruit_1
    print(fruit_1)
result = ngword in fruit_2
if(result == True):
    group = fruit_2
    print(fruit_2)
result = ngword in fruit_3
if(result == True):
    group = fruit_3
    print(fruit_3)
result = ngword in fruit_4
if(result == True):
    group = fruit_4
    print(fruit_4)
result = ngword in fruit_5
if(result == True):
    group = fruit_5
    print(fruit_5)
result = ngword in fruit_6
if(result == True):
    group = fruit_6
    print(fruit_6)

result = ngword in food_1
if(result == True):
    group = food_1
    print(food_1)
result = ngword in food_2
if(result == True):
    group = food_2
    print(food_2)
result = ngword in food_3
if(result == True):
    group = food_3
    print(food_3)
result = ngword in food_4
if(result == True):
    group = food_4
    print(food_5)
result = ngword in food_5
if(result == True):
    group = food_5
    print(food_5)
result = ngword in food_6
if(result == True):
    group = food_6
    print(food_6)

result = ngword in vehicle_1
if(result == True):
    group = vehicle_1
    print(vehicle_1)
result = ngword in vehicle_2
if(result == True):
    group = vehicle_2
    print(vehicle_2)
result = ngword in vehicle_3
if(result == True):
    group = vehicle_3
    print(vehicle_3)
result = ngword in vehicle_4
if(result == True):
    group = vehicle_4
    print(vehicle_4)
    
    
result = ngword in animal_1
if(result == True):
    group = animal_1
    print(animal_1)
result = ngword in animal_2
if(result == True):
    group = animal_2
    print(animal_2)
result = ngword in animal_3
if(result == True):
    group = animal_3
    print(animal_3)
result = ngword in animal_4
if(result == True):
    group = animal_4
    print(animal_4)
result = ngword in animal_5
if(result == True):
    group = animal_5
    print(animal_5)
result = ngword in animal_6
if(result == True):
    group = animal_6
    print(animal_6)
    
result = ngword in building_1
if(result == True):
    group = building_1
    print(building_1)
result = ngword in building_2
if(result == True):
    group = building_2
    print(building_2)
result = ngword in building_3
if(result == True):
    group = building_3
    print(building_3)
result = ngword in building_4
if(result == True):
    group = building_4
    print(building_4)
result = ngword in building_5
if(result == True):
    group = building_5
    print(building_5)
result = ngword in building_6
if(result == True):
    group = building_6
    print(building_6)
