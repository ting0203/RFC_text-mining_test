import pandas as pd

import nltk

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('english')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk.corpus import stopwords
stops = stopwords.words('english')
from string import punctuation

testStr = "This value is also called cut-off in the literature. If float, the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None."

##做斷詞
tokens = nltk.word_tokenize(testStr)
print(tokens)
tokens = nltk.wordpunct_tokenize(testStr) ## 請注意，差異在內文的cut-off
print(tokens)

##stemming和lemmatize是一個把所有不同時態或是不同變化相同的字變成同一個字。
##而stemming比較像是去掉ed或是s這種添加在字後面的小字母，lemmatize則是字根化，就是把字還原到字根的型態。
##以下讓我們來看一下示範。
df = pd.DataFrame(index = tokens)
df['porter_stemmer'] = [porter_stemmer.stem(t) for t in tokens]
df['lancaster_stemmer'] = [lancaster_stemmer.stem(t) for t in tokens]  ##去除字尾如:ed, s
df['snowball_stemmer'] = [snowball_stemmer.stem(t) for t in tokens]
df['wordnet_lemmatizer'] = [wordnet_lemmatizer.lemmatize(t) for t in tokens]  ##字根化
print(df)

##前處理，英文字轉成小寫
##使用停用詞
df = pd.DataFrame(index = [t for t in tokens if t not in stops])
df['porter_stemmer'] = [porter_stemmer.stem(t.lower()) for t in tokens if t not in stops]
df['lancaster_stemmer'] = [lancaster_stemmer.stem(t.lower()) for t in tokens if t not in stops]
df['snowball_stemmer'] = [snowball_stemmer.stem(t.lower()) for t in tokens if t not in stops]
df['wordnet_lemmatizer'] = [wordnet_lemmatizer.lemmatize(t.lower()) for t in tokens if t not in stops]
print(df)
