#dictionary

"""
    辞書はユニークキーと値のペアを要素として格納するコンテナ
    要素に順序はない
    ユニークキーに重複があってはいけない
    値は重複していてもよい

    辞書 = { キー:値, キー:値, キー:値, ・・・ }
    のようにして辞書コンテナを作成する

    辞書もオブジェクトの一種なので、カンマ区切りでメソッドが使える。

    なんというか、配列のインデックスが数字じゃなくて任意になった感じがする。。。
"""

#辞書の定義
freet1 = {"秋月":"駆逐", "時雨": "駆逐", "五十鈴": "軽巡", "摩耶": "重巡"}

#要素数の取得：len
print(len(freet1)) #4

#要素の指定：キーを入れて値の出力：get
print(freet1.get("五十鈴")) #軽巡
print(freet1.get("翔鶴")) #None

#辞書の更新：update
additional = {"金剛":"戦艦", "赤城":"空母"}
freet1.update(additional)
print(freet1)

#要素の削除：del
del freet1["秋月"] #辞書は中かっこだが、削除は要素に対して行われるので、大かっこを使う事に注意
print(freet1)

#キーが辞書に含まれているか確認：in
print("時雨" in freet1) #True
print("時雨" not in freet1) #False

#辞書のキーリスト（辞書のキーだけのリストを得る）：list(辞書.keys())
print(list(freet1.keys()))

#辞書の値リスト（辞書の値だけのリストを得る）：list(辞書.values())
print(list(freet1.values()))

#辞書の繰り返し処理：for キー, 値 in 辞書.items()
for tmp_key, tmp_value in freet1.items():
    print(tmp_key, tmp_value)
