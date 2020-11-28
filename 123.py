from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

stopwords = set(stopwords.words('english') + list(punctuation))
max_cut = 0.9
min_cut = 0.1

"""
計算出每個詞出現的頻率word_sent是一個已經分好詞的列表
返回一個詞典freq[],freq[w]代表了w出現的頻率
"""
def compute_frequencies(word_sent):
    #print(word_sent)
    #print(type(word_sent))
    """
    defaultdict和普通的dict
    的區別是它可以設定default值
    引數是int預設值是0
    """
    freq = defaultdict(int)
    #print(freq)
    #print(type(freq))
    #統計每個詞出現的頻率
    for s in word_sent:
        for word in s:
            #注意stopwords
            if word not in stopwords:
                #print(freq[word])
                freq[word] += 1
                #得出最高出現頻次m
                #print(freq.values())
                #print(max(freq.values()))
                m = float(max(freq.values()))
    #所有單詞的頻次統除m
    for w in list(freq.keys()):
        freq[w] = freq[w]/m
        if freq[w] >= max_cut or freq[w] <= min_cut:
            #print("4")
            del freq[w]
            # 最後返回的是
            # {key:單詞, value: 重要性}
    return freq

def summarize(text, n):
    """
    用來總結的主要函式
    text是輸入的文字
    n是摘要的句子個數
    返回包含摘要的列表
    """
    # 首先先把句子分出來
    sents = sent_tokenize(text)
    #print(sents)
    assert n <= len(sents)
    # 然後再分詞
    word_sent = [word_tokenize(s.lower()) for s in sents]   #以句號為一斷點
    #print(word_sent[1])
    # freq是一個詞和詞重要性的字典
    freq = compute_frequencies(word_sent)
    #ranking則是句子和句子重要性的詞典
    ranking = defaultdict(int)
    for i, word in enumerate(word_sent):
        #print("1")
        for w in word:
            #print("2: " + w)
            #print("2: " + freq)            
            if w in freq:
                #print("3")
                ranking[i] += freq[w]
                sents_idx = rank(ranking, n)
                return [sents[j] for j in sents_idx]
    """
    考慮到句子比較多的情況用遍歷的方式找最大的n個數比較慢
    我們這裡呼叫heapq中的函式建立一個最小堆來完成這個功能
    返回的是最小的n個數所在的位置
    """
def rank(ranking, n):
    return nlargest(n, ranking, key=ranking.get)

if __name__ == '__main__':
    with open("rfc2734.txt", "r") as myfile:
        text = myfile.read().replace('\n','')
        res = summarize(text, 2)
        for i in range(len(res)):
            print(res[i])
