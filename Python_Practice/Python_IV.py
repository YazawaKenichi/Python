from menu_item import MenuItem
#menu_item がないから正しく動かない
#サイトを解析するか、コード読んで自作するしかない。がんばれ。（他力本願）

menu_item1 = MenuItem("サンドイッチ", 500)
menu_item2 = MenuItem("チョコケーキ", 400)
menu_item3 = MenuItem("コーヒー", 300)
menu_item4 = MenuItem("オレンジジュース", 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + ". " + menu_item.info())
    index += 1

print("--------------------------------------")

order = int(input("メニューの番号を入力してください。："))
selected_menu_item = menu_items[order]
print("選択されたメニュー：" + selected_menu_item.name)

count = int(input("個数を入力してください。（３個以上で１割引き）："))
result = selected_menu_item.get_total_price(count)
print("合計は " + str(result) + " 円です。")

"""
プログラミングでメニューという「もの」を生成するには、
まずはその「設計図」を用意する必要がある。
「設計図」の事を「クラス」という。
「もの」の事をインスタンスと呼ぶ。

具体例
「メニュー」には「名前」と「値段」の情報がある
「メニュー」が「クラス」
「名前」や「値段」がインスタンス。

インスタンスは次の流れに沿って生成する。
Step.1
クラス（設計図（メニュー））を用意する。
Step.2
クラス（設計図（メニュー））から空のインスタンス（名前や値段）を生成する。
Step.3
インスタンス（名前や値段）に情報を追加する。

クラスの定義
class クラス名:
で定義できる
クラス名は大文字で始めるようにするらしい、
これは文法やルールというより、モラルみたいなものかもしれない。
詳しくはもう少し研究が必要。

クラスの中身（設計図の内容）は「class クラス名:」の後の行でインデントして記述。
何も処理がないときは pass と記述する。
例
class Class_Name: #クラス名の定義
    pass #何も処理がないときの記述
"""
