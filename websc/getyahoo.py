import requests

url = "https://news.yahoo.co.jp"

response = requests.get(url)    # url の情報を取得する  # 今回は HTML スクリプトを取得する

print(response.text)    # 取得した情報のテキストを表示

