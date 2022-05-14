import requests
import re

domain = 'https://www.tuyano.com'
prm = {'id' : 511001}
resp = requests.get(domain + '/index3?id~511001')
data = resp.text

fdata = re.findall(r'<img src\s*=\s*"([^"]+)"', data)
print('*** image address ***')

n = 1

for item in fdata:
    result = requests.get(domain + item)
    fname = "saved_" + str(n)
    ctype = result.headers['Content-Type']    # ファイルの種類を取得
    if(ctype == "image/jpeg"):
        fname += ".jpg"
    if(ctype == "image/png"):
        fname += ".png"
    if(ctype == "image/gif"):
        fname += ".gif"
    with open(fname, 'wb') as file:
        file.write(result.content)
        print("save file " + fname)
    n += 1

