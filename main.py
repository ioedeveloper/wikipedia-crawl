import requests
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/Web_content")
html = response.text
soup = BeautifulSoup(html)
print(soup.p.a)