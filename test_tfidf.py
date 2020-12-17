from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

text = open('rfc1883.txt', 'r').read()
text1 = open('rfc1702.txt', 'r').read()
text2 = open('rfc2734.txt', 'r').read()
documents = [text,text1,text2]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
# X2 = vectorizer2.fit_transform(documents)
# print(vectorizer2.get_feature_names())


true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]


terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print


