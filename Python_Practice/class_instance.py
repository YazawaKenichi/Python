"""
クラスインスタンスの生成
下記のようにクラス名（）とそのインスタンスを呼び出すことで、
クラス（設計図）を用いて新しくインスタンスを生成することができる。
class MenuItem:
    pass
menu_item1 = MenuItem() #MenuItem  クラスからインスタンスを生成
MenuItem() は MenuItem クラスからインスタンスを生成することを表す。
menu_item1 にそれを格納している。
一般化すると
変数名 ＝ クラス名（）
とすることで、生成したインスタンスを変数に代入することができる。
"""

#クラスの定義
class MenuItem:
    pass

#インスタンスを生成して menu_item1 に格納
menu_item1 = MenuItem()
