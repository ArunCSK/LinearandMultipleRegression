#import Libararies
import numpy as np
import re
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

##download and install nltk
#import nltk
#nltk.download()

DataSet = pd.read_csv("Restaurant_Reviews.tsv",delimiter="\t")
#print(DataSet)

sentence = []

for i in range(len(DataSet)):
    sentence.append((DataSet['Review'][i]))

print(sentence)

corpus = []

for i in range(0, len(DataSet)):
    review = re.sub('[^a-zA-Z]', ' ', DataSet['Review'][i])
    #review = review.split()
    review = word_tokenize(review)
    #print(review)
    ps = PorterStemmer()

    [ps.stem(word) for word in review
     if not word in set(stopwords.words('english'))]

    review = ' '.join(review)

    corpus.append(review)

cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = DataSet.iloc[:, 1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25 , random_state = 0)

model = RandomForestClassifier(n_estimators= 501, criterion='entropy')
#model = LogisticRegression()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print(y_pred)

cm = confusion_matrix(y_test, y_pred)
print(cm)

score = accuracy_score(y_test, y_pred)
print(score)