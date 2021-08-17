#set

niji_list = ["上原歩夢", "優木せつな", "宮下愛", "中須かすみ", "桜坂しずく", "天王寺璃奈", "近江彼方", "朝香果林", "エマ・ヴェルデ"]
niji_set = set(niji_list) #リストからセットを生成
print(niji_set)

#セット動詞で差分を取るなど、演算ができる
QU4RTZ_set = set(["中須かすみ", "天王寺璃奈", "近江彼方", "エマ・ヴェルデ"])
print(niji_set ~ QU4RTZ_set) #QU4RTZ にいない niji の要素
print(niji_set | QU4RTZ_set) #QU4RTZ または niji の要素
print(niji_set & QU4RTZ_set) #QU4RTZ かつ niji の要素
print(niji_set ^ QU4RTZ) #QU4RTZ と niji のうち片方だけにある要素

#ある要素がセットに含まれているか確認
set = set(["Python", "Java"])
print("Python" in set) #True
print("Python" not in セット) #False

#セット要素の追加：add
set.add("Ruby")

#セット要素の削除：remove
set.remove("Python")

#セットの繰り返し処理（セットの要素を順次処理していく（リストと同様））
for tmp in set:
    print(tmp)

"""
    セットは要素の重複がないコンテナ。
    要素の順序も必要ない。
    set 関数にリストを渡して生成。

    コンテナには、リスト・タプル・セット・辞書の四種がある。
"""
