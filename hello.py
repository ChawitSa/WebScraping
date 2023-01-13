from bs4 import  BeautifulSoup
print(BeautifulSoup("<p>Some<b>bad<i>HTML").prettify())