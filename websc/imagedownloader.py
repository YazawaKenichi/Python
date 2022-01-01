import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import cv2

root = "https://www.nogizaka46.com/"
url = "https://www.nogizaka46.com/photo/"
store_path = "./"

def img_store(path):
    img = requests.get(path).content
    print(path)
    with open(store_path, "wb") as f:
        f.write(img)
    img_local = cv2.cvtColor(cv2.imread(store_path), cv2.COLOR_BGR2RGB)
    plt.imshow(img_local)
    plt.show()

f = open('Debug.html', 'w', encoding='utf-8')
response = requests.get(url)
# print(response.text)
f.write(response.text)
f.close()
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("div", id="photomain2"))
top_img = soup.find("div", id="photomain2").find("div").find("img").get("src")
img_store(root + top_img)

