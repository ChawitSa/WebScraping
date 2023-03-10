from bs4 import  BeautifulSoup
import requests
import  pandas as pd
import xlsxwriter


destination = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
soup = BeautifulSoup(destination.content, 'html.parser')
list = []
for i in soup.findAll(class_ = "title"):
    sub_list = []
    sub_list.append(i.get("title"))
    sub_list.append("https://webscraper.io"+i.get("href"))
    list.append(sub_list)
title = pd.DataFrame(list)
print(title)
writer = pd.ExcelWriter("WebTest.xlsx", engine="xlsxwriter")
title.to_excel(writer, sheet_name="หน้าแรก")
writer.save()
