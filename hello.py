from bs4 import  BeautifulSoup
import requests
import  pandas as pd


destination = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
soup = BeautifulSoup(destination.content, 'html.parser')
list = []
for i in soup.findAll(class_ = "title"):
    list.append(i.get("title"))
title = pd.DataFrame(list)
print(title)

