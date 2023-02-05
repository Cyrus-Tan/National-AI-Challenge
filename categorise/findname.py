import pandas as pd

import re, string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

import pickle

data = pd.read_csv('../scrape/info2.csv')

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=69)

print('Training Data :', X_train.shape)

print('Testing Data : ', X_test.shape)

cv = CountVectorizer()

X_train_cv = cv.fit_transform(X_train)

X_train_cv.shape

lr = LogisticRegression(max_iter=3000)

model2 = lr.fit(X_train_cv, y_train)

vec_file = 'vectorizer.pickle'
pickle.dump(cv, open(vec_file, 'wb'))

mod_file = 'classification.model'
pickle.dump(model2, open(mod_file, 'wb'))
