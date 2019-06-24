#import Libararies
import numpy as np
import re
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer


##download and install nltk
#import nltk
#nltk.download()

DataSet = pd.read_csv("Restaurant_Reviews.tsv",delimiter="\t")
#print(DataSet)

sentence = []

for i in range(len(DataSet)):
    sentence.append((DataSet['Review'][i]))

#print(sentence)

corpus = []

for i in range(0, len(DataSet)):
    review = re.sub('[^a-zA-Z]', ' ', DataSet['Review'][i])
    review = review.split()
    #print(review)
    ps = PorterStemmer()

    [ps.stem(word) for word in review
     if not word in set(stopwords.words('english'))]

    review = ' '.join(review)

    corpus.append(review)