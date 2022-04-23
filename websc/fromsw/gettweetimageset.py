# coding: UTF-8

'''
    一体どんな動作をしているのだろうか....
    そもそも何のプログラムなのだろうか....
    データが取得出来てない気がする。
'''

from urllib3 import PoolManager
import urllib    # HTTP 通信を扱うためのモジュール
import os
import json
from datetime import datetime   # 日付や時間の文字列変換に使えるモジュール

TOKEN = "86yVwPR2I39bmq8kVVSVFGmEBeC9YnwoZsjXSsdcaE1eaU1Gvw"

headers = {'Authorization': 'Bearer ' + TOKEN}
'''
    headers は辞書型配列。
    Authorization をインデックスとして使用すると
    'Bearer ' + os.getenv("TWITTER_TOKEN") の結合された文字列が取得できる。

    os.getenv
    環境変数 key が存在すればその値を返し、存在しなければ default を返す。
    環境変数に TWITTER_TOKEN を追加する必要がある。
    この token がどの token かわからない
'''
search_word = "#絵描きさんとつながりたい -is:retweet -is:reply"
num_result = 100
http = PoolManager()
'''
    PoolManager()
    インスタンスの初期化
'''
search_url = 'https://api.twitter.com/2/tweets/search/recent'
params = {
        'query': search_word,
        'expansions': 'author_id,attachments.media_keys',
        'media.fields': 'type,url,width,height',
        'tweet.fields': 'id,created_at,lang,text,entities,public_metrics',
        'user.fields': 'id,name,username,public_metrics',
        'max_results': num_result
#        'next_token': ''
        }

req = http.request('GET',
        search_url,
        headers=headers,
        fields=params)
'''
    HTTP のリクエストの構造
    一行目には
    > Method : GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH の９種類がある。それぞれの意味は https://developer.mozilla.org/ja/docs/Web/HTTP/Methods を参照。
    > URL : 
    > HTTP_Version : 
    二行目以降には
    > User-Agent : ブラウザの種類や OS 情報、検索エンジンクローラの名前
    > Referer : どのページから生じたリクエストなのか
    > Cookie : ブラウザを特定するためのデータ
    > Accept : どのようなデータを受け取りたいのか
    > Accept-Language : 言語
    > Accept-Encoding : 文字コード
    > Accept-Charset : 画像の種類
    > If-Modified-Since / If-None-Match : ブラウザに保存されているローカルキャッシュが変更されているかどうかを問い合わせる

    PoolManager().request("GET", url, 

    「リクエスト」はブラウザがサーバに必要なデータを送信すること。
    これに対して「レスポンス」がある。こちらはサーバがリクエストに応じてブラウザに返すデータを送信すること。
    どちらも HTTP 接続のため、「HTTP ヘッダー」と「データ本体」の構造を持っている。
    今回のプログラムでは http.request とされているので「リクエスト」だけ考えれば良い。

    GET Method : 指定したリソースの表現をリクエストする。データの取り込みのみ。
'''

mapping = json.loads(req.data)



