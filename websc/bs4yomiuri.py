import requests
from bs4 import BeautifulSoup

url = "https://www.yomiuri.co.jp"

res = requests.get(url)

# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")   # html.parser のパーサーを与える
elems = soup.select("body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-of-type(1) > div > h3 > a")

print(elems[0].contents[0])

