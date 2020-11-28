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


stopwords_word = set(stopwords.words('english'))

text = open('rfc2734.txt', 'r').read()
token = word_tokenize(text)
#print(token)

fdist = FreqDist(token)
'''
for key in fdist:
    print(key, fdist[key])
'''
text1 = word_tokenize(text.lower())
#print(text1)
stopwords = [x for x in text1 if x not in stopwords_word]
print(stopwords)

'''
fdist = FreqDist(stopwords)
fdist.plot(30,cumulative=False)
plt.show()
'''





