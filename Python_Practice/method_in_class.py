#メソッド
#一行コメは予想
"""複数行コメは答え合わせ"""

class Example():
    def __init__(self, a, b, c):
        self.num1 = a #インスタンスに num1 属性を定義して a を代入する
        self.num2 = b
        self.num3 = c

    def print_tot(self): #コンストラクタに self 引数は必須
        tot = self.num1 + self.num2 + self.num3 #tot に a + b + c の値を代入する
        print(tot) #値を表示する

myinstance = Example(1, 2, 3)
#myinstance 変数を生成し、Example クラスからインスタンスを生成
#init コンストラクタの引数 a, b, c にそれぞれ 1, 2, 3 を渡す。
"""コンストラクタとは init それだけを指すみたいだ"""
"""クラス内にはコンストラクタと print_tot メソッドがある事になる"""
"""コンストラクタ引数に指定した a, b, c を、属性 num1, num2, num3 に代入した"""
"""ClassName(引数) でコンストラクタを作ると、引数は init の引数扱いになるようだ"""
"""print_tot() は生成したインスタンスが持つ属性三つの合計を計算して出力する。"""

myinstance.print_tot()
#print_tot() コンストラクタを実行する

"""
Python においては、メソッドをクラス内に定義された関数に限定して呼ぶのかもしれない。
サイトを見た感じそんな雰囲気ある。
メソッドはインスタンスのふるまいや行動を表現できる。


"""
