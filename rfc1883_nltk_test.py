from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
import re


#stopwords_word = set(stopwords.words('english'))
stopwords_word = nltk.corpus.stopwords.words('english')
newStopWords = [',','|','.','--',':','(',')']
stopwords_word.extend(newStopWords)

text = open('rfc1883_1.txt', 'r').read()
token = word_tokenize(text)
#print(token)

str6 = "，".join(token)  #轉換成字串

f = open('file_io.txt', 'w')    #寫入檔案
f.write(str6)
f.close()

fdist = FreqDist(token) #計算文字次數

#for key in fdist:
#    print(key, fdist[key])     #印出文字次數

text1 = word_tokenize(text.lower()) #全部文字轉換成小寫
#print(text1)
stopwords = [x for x in text1 if x not in stopwords_word]   #使用停止詞篩選
#print(stopwords)

fdist1 = FreqDist(stopwords)
for key in fdist1:
    print(key, fdist1[key])
    
#畫出折線圖

'''
fdist = FreqDist(stopwords)
fdist.plot(30,cumulative=False)
plt.show()
'''





