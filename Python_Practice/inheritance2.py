#継承
#予想
"""答え合わせ"""

#Oya クラスを作成
class Oya(): #Oya クラスの定義
    def oya_func(self): #コンストラクタは必要ないが、メソッドの引数に self は必須。
        print("I am OYA") #Oya クラスの oya_func メソッドの処理を定義

#Kodomo クラスを作成
class Kodomo(Oya): #Kodomo クラスは Oya クラスを継承する。
    def kodomo_func(self): #コンストラクタは必要ないが、メソッドの引数に self は必須。
        print("I am Kodomo") #Kodomo クラスの kodomo_func メソッドの処理を定義

k = Kodomo() #Kodomo インスタンスを生成し、変数 k に代入。

k.oya_func() #Kodomo クラスは Oya クラスを継承しているから、oya_func メソッドを呼び出せる。
k.kodomo_func() #当然 Kodomo クラスにある kodomo_func メソッドも使える。
