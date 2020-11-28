# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
# sample text for performing tokenization使用斷詞
text = '''In Brazil they drive on the right-hand side of the road.
Brazil has a large coastline on the eastern side of South America'''
# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
print(token)

# finding the frequency distinct in the tokens計算單詞數
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
#print(fdist.tabulate())

#畫出折線圖
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

#印出單詞數
for key in fdist:
    print(key, fdist[key])

#去除尾端字
from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem("waiting")
print(pst.stem("waiting"))

#使用停用詞
# importing stopwors from nltk library
from nltk import word_tokenize
from nltk.corpus import stopwords
a = set(stopwords.words('english'))
text = "Cristiano Ronaldo was born on February 5, 1985, in Funchal, Madeira, Portugal."
text1 = word_tokenize(text.lower())
print(text1)
stopwords = [x for x in text1 if x not in a]
print(stopwords)
