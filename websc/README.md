### WEB Scraping で使える情報置き場
<hr>
<br>
```
$ pip install requests beautifulsoup4 selenium
$ sudo dpkg -i chromium-chromedriver_61.0.3163.79-0ubuntu0.14.04.1196_armhf.deb
```
<br>
ライブラリのインポート<br>
```
import requests
from bs4 import BeautifulSoup
``` 
<br>
```
Requests API
  get() # 取得
  post()  # 登録
  put() # 更新
  delete()  # 削除
  head()
  options()
```
WEB Scraping に使われるのは requests.get() のみ。<br>
<br>
HTML 全体を取得する。<br>
```
response = requests.get(URL)
```
属性値<br>
```
requests.get():
  text  # 内容
  content # バイナリデータ
  status_code # ステータスコード
```
status_code は、404 Not Found などのコードのこと。<br>
text はそのまま print すると HTML 全体が出力される。<br>
string 型のようで、文字列配列としてふつーに処理できる。（例えば```requests.get(URL).content[:300]```とか)<br>
contnet<br>
<br>
Beautiful Soup の利用（[公式ドキュメント](http://kondou.com/bs4/)）
取得した情報を解析する<br>
```
soup = BeautifulSoup(response.text, parser)
```
上記は BeautifulSoup のインスタンスを生成している。
parser は解析方法の指定。いくつかあるが、```"html.parser"``` としておけば今はとりあえず大丈夫な気がする。（BeautifulSoup4 公式サイトによると速度の問題があるっぽい）<br>
BeautifulSoup の中身はドキュメントを入れ子構造で表現している。<br>
```
class BeautifulSoup:
  find(tag)
  find(id=idname)
  get_text()
  contents[]
```
tag は HTML タグを string 型で指定する。<br>
idname は HTML id を string 型で指定する。<br>
同じノリで class も指定できるが、こちらは抽象データ型の class と衝突してしまうので ```class_=classname``` とする。<br>
get_text() とすると、タグを除去した状態のテキストデータだけを抽出することが可能。<br>
contents[] は一番外のタグで囲まれた中身を抽出することができる。中身が複数になることも十分あるので、配列となっている。<br>
階層を下へ下へと移動する方法として、以下のようなことが可能。<br>
```
elems = soup.body # body に移動
elems = soup.body.a # body 内一番最初の a に移動
elems = soup.body.find_all("a") # body 内 a をすべて抽出
elems = soup.body.find("a", id="idname").b  # body 内 id="idname" 内一番最初の b に移動
elems = soup.body.find("a", id="idname").find("b")  # body 内 id="idname" 内一番最初の b に移動
```
elems は配列として扱うことも可能で、elems[0] とすれば、find_all で一番最初にマッチしたものを選択することができ、elems[1] とすれば２つ目を選択することができる。
なんでなのかよくわからなかったが、href の中で "hogehoge" が含まれているもののみをすべて抽出する方法が
```
import re
elems = soup.find_all(href=re.compile("hogehoge"))
```
らしい、re ライブラリを使ったことがないから何をしているんだかしているんだか全くわからん。ただここからいくぶんか応用はできそう。
また、
```
soup.find().atters['href']
```
とすることで href の内容だけを抽出することができる。

Javascript を使った動的ページへの対応
Selenium を用いて WEB Scraping
環境構築は[ここ](https://qiita.com/Brutus/items/7381a13fa395f9b73855)に任せる。
```
import sys
sys.patch.append('/home/pi/.local/lib/python3.7/size-packages/')
from selenium import webdriver
```
最初の二行
二行は Raspberry Pi で WEB Scraping したい場合に記述する。
Chrome の Web Driver と Chromium の Web Driver は違うので環境によって記述が少々異なる。
```
browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
```
はっきり言ってはっきり言ってこれが何をしているのかさっぱりわからない。
なんとなく、Chromium の場所を特定してそうな気がする。
```browser.get(URL)``` で URL のウェブサイトを開くことができる。
```
search_bar = driver.find_element_by_name("q") # 検索バーを取得
search_bar.send_key("hogehoge") # hogehoge を検索バーに入力
search_bar.submit() # 検索実行
```



