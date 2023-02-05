import pandas as pd
import pickle

data1 = pd.read_csv('../scrape/test.csv')

text = list(data1['text'])

loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))

# load the model
loaded_model = pickle.load(open('classification.model', 'rb'))

# make a prediction
print(loaded_model.predict(loaded_vectorizer.transform(text)))