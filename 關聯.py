import re
## The first paragraph of Wikipedia's article on itself - you can try with other pieces of text with preferably more words (to produce more meaningful word pairs)
#text = open("123.txt", "r").read()
text = "Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger.[10] Sanger coined its name,[11][12] as a portmanteau of wiki[notes 3] and 'encyclopedia'. Initially an English-language encyclopedia, versions in other languages were quickly developed. With 5,748,461 articles,[notes 4] the English Wikipedia is the largest of the more than 290 Wikipedia encyclopedias. Overall, Wikipedia comprises more than 40 million articles in 301 different languages[14] and by February 2014 it had reached 18 billion page views and nearly 500 million unique visitors per month.[15] In 2005, Nature published a peer review comparing 42 science articles from Encyclopadia Britannica and Wikipedia and found that Wikipedia's level of accuracy approached that of Britannica.[16] Time magazine stated that the open-door policy of allowing anyone to edit had made Wikipedia the biggest and possibly the best encyclopedia in the world and it was testament to the vision of Jimmy Wales.[17] Wikipedia has been criticized for exhibiting systemic bias, for presenting a mixture of 'truths, half truths, and some falsehoods',[18] and for being subject to manipulation and spin in controversial topics.[19] In 2017, Facebook announced that it would help readers detect fake news by suitable links to Wikipedia articles. YouTube announced a similar plan in 2018."
text = re.sub("[\[].*?[\]]", "", text)     ## Remove brackets and anything inside it.
text=re.sub(r"[^a-zA-Z0-9.]+", ' ', text)  ## Remove special characters except spaces and dots
text=str(text).lower()                     ## Convert everything to lowercase
## Can add other preprocessing steps, depending on the input text, if needed.
import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
desirable_tags = ['NN'] # We want only nouns - can also add 'NNP', 'NNS', 'NNPS' if needed, depending on the results
word_list = []
for sent in text.split('.'):
    for word in sent.split():
        '''
        Extract the unique, non-stopword nouns only
        '''
        if word not in word_list and word not in stop_words and nltk.pos_tag([word])[0][1] in desirable_tags:
            word_list.append(word)
'''
Construct the association matrix, where we count 2 words as being associated 
if they appear in the same sentence.
Later, I'm going to define associations more properly by introducing a 
window size (say, if 2 words seperated by at most 5 words in a sentence, 
then we consider them to be associated)
'''
import numpy as np
import pandas as pd
table = np.zeros((len(word_list),len(word_list)), dtype=int)
for sent in text.split('.'):
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if word_list[i] in sent and word_list[j] in sent:
                table[i,j]+=1
df = pd.DataFrame(table, columns=word_list, index=word_list)
# Count the number of occurrences of each word in word_list
all_words = pd.DataFrame(np.zeros((len(df), 2)), columns=['Word', 'Count'])
all_words.Word = df.index
for sent in text.split('.'):
    count=0
    for word in sent.split():
        if word in word_list:
            all_words.loc[all_words.Word==word,'Count'] += 1
# Sort the word pairs in decreasing order of their association strengths
df.values[np.triu_indices_from(df, 0)] = 0 # Make the upper triangle values 0
assoc_df = pd.DataFrame(columns=['Word 1', 'Word 2', 'Association Strength (Word 1 -> Word 2)'])
for row_word in df:
    for col_word in df:
        '''
        If Word1 occurs 10 times in the text, and Word1 & Word2 occur in the same sentence 3 times,
        the association strength of Word1 and Word2 is 3/10 - Please correct me if this is wrong.
        '''
        assoc_df = assoc_df.append({'Word 1': row_word, 'Word 2': col_word, 
                                        'Association Strength (Word 1 -> Word 2)': df[row_word][col_word]/all_words[all_words.Word==row_word]['Count'].values[0]}, ignore_index=True)
assoc_df.sort_values(by='Association Strength (Word 1 -> Word 2)', ascending=False)
print(assoc_df)

