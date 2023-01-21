import requests

url = 'https://www.fairprice.com.sg/categories'

information = requests.get(url).text

split_information = information.split(" ")

categories = ""
for item in split_information:
    if 'href="/category/' in item:
        intermediate = item.replace('href=', "").replace('"', "")
        if categories != "":
            categories += "\n"
        categories += f"https://www.fairprice.com.sg{intermediate}"

with open("categorylinks.txt", "w") as link_file:
    link_file.write(categories)

