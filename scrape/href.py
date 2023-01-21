import requests

url = 'https://www.fairprice.com.sg/categories'

information = requests.get(url).text

split_information = information.split(" ")

categories = ""

for item in split_information:
    if 'href="/category/' in item:
        if categories != "":
            categories += "\n"
        if item not in categories:
            categories += item

while True:
    if "\n\n" in categories:
        categories = categories.replace("\n\n", "\n")
    else:
        break

categories = categories.replace('"', "").replace('href=', "https://www.fairprice.com.sg")
with open("categorylinks.txt", "w") as link_file:
    link_file.write(categories)

