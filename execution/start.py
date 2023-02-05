import os
import time
import pandas as pd
import pickle
import expiry.py

lst = os.listdir(os.getcwd() + '/input')
number_files = len(lst)

if number_files > 1:
    raise Exception("Please upload only one image")
elif number_files == 0:
    raise Exception("Please upload only an image")

with open("interfile/recognized.txt", "w"):
    pass

with open("interfile/recognized.csv", "w") as csv_file:
    csv_file.write(",text\n")

os.system(f"python interfile/receiptreader.py --image {os.getcwd()}/input/{lst[0]}")

time.sleep(1)


with open("interfile/recognized.txt", "r") as txt_file:
    lines = txt_file.readlines()

line_counter = 1
for i in lines:
    if i == "\n":
        pass
    else:
        with open("interfile/recognized.csv", "a") as csv_file:
            csv_file.write(f"{line_counter}, {i}")
        line_counter += 1

data1 = pd.read_csv('interfile/recognized.csv')

text = list(data1['text'])

loaded_vectorizer = pickle.load(open('interfile/vectorizer.pickle', 'rb'))

# load the model
loaded_model = pickle.load(open('interfile/classification.model', 'rb'))

# make a prediction
print(loaded_model.predict(loaded_vectorizer.transform(text)))