import os
import time
import pandas as pd
import pickle
from interfile.expiry import exp_dates
from datetime import timedelta, date

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
catego = list(loaded_model.predict(loaded_vectorizer.transform(text)))
today = date.today()

with open("interfile/recognized.csv", "r") as csv_file:
    lines2 = csv_file.readlines()

for i in range(1, len(lines2)):
    updated = lines2[i].rstrip("\n")
    with open('information.csv', 'a') as information_file:
        information_file.write(f"{updated}, {catego[i - 1]}, {date.strftime(today + timedelta(days=exp_dates[catego[i - 1]]), '%m/%d/%y')}\n")

