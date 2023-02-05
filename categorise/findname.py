import pandas as pd
import numpy as np

import re, string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import roc_curve, auc, roc_auc_score

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import pickle

data = pd.read_csv('../scrape/info.csv')

data['target'].value_counts(normalize = True).plot.bar()

text = list(data['text'])

lemmatizer = WordNetLemmatizer()

corpus = []

for i in range(len(text)):

    r = re.sub('[^a-zA-Z]', ' ', text[i])

    r = r.lower()

    r = r.split()

    r = [word for word in r if word not in stopwords.words('english')]

    r = [lemmatizer.lemmatize(word) for word in r]

    r = ' '.join(r)

    corpus.append(r)

#assign corpus to data['text']

data['text'] = corpus

data.head()

X = data['text']

y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

print('Training Data :', X_train.shape)

print('Testing Data : ', X_test.shape)

cv = CountVectorizer()

X_train_cv = cv.fit_transform(X_train)

X_train_cv.shape

lr = LogisticRegression(max_iter=3000)

model2 = lr.fit(X_train_cv, y_train)

vec_file = 'vectorizer.pickle'
pickle.dump(cv, open(vec_file, 'wb'))

# filename = 'finalized_model.sav'
# joblib.dump(lr, filename)

# X_test_cv = cv.transform(X_test)
# print(cv)

mod_file = 'classification.model'
pickle.dump(model2, open(mod_file, 'wb'))

# loaded_model = joblib.load("finalized_model.sav")
#
# data1 = pd.read_csv('../scrape/test.csv')
#
# text = list(data1['text'])
#
# X_test_cv = cv.transform(text)
#
# result = loaded_model.predict(X_test_cv)
# print(result)
