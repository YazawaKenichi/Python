class Point:
    pass

point1 = Point()
print(type(point1))

#出力結果
# <class '__main__.Point'>

"""
    string = "Hello, World!"
    print(type(string))
    とすると、出力結果は <class 'str'> となる、
    これは、string という変数が str 型であることを表し、str 型はクラスであることも同時に示している。

    そして本プログラムでは、Point という新しい型（厳密にはクラス）を定義して point1 にその型（インスタンス）を代入（生成）している。
    <class 'str'> と違うのは __main__ という文字列が一緒に出力されている事である。
    __main__ というのは何らかの形で Python の対話環境を利用している場合に、そのコードを実行する環境を表すもの。
    つまり、<class '__main__.HogeHoge'> となっていたら HogeHoge というクラスは対話環境で定義されたクラスであるということがわかる。
    <class '__main__.PiyoPiyo'> となっていれば、PiyoPiyo というクラスも対話環境で定義されたクラスであるということがわかる。
    また、同時に、point1 という変数が Point 型変数であることがわかる。
"""

"""
    クラスを定義すると Python のオブジェクトが持つ基本的な機能が備わるようになっている。
    これを調べるには dir 関数が使える。
    dir(obj)
    dir() 関数
    obj 属性を知りたいオブジェクト

    dir 関数の引数にオブジェクトを渡すと、そのオブジェクトが持つ「属性」を調べてくれる。
    
    下のコードはその機能を用いて Point 型の point1 がどんな属性を持っているのか調べる。
"""
print(dir(point1))
#出力結果
#<class '__main__.Point'>
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

"""
    Point クラスの定義は pass しかないのに、__hoge__ のような属性がたくさん表示される。
    これらは、Python が「すべてのオブジェクトの基盤」となるクラスとして、「object クラス」から来ている。
    class HogeHoge: とクラスを定義すると、object クラスから新しいクラスへと自動で継承されるようになっている。
    つまり以下に書き換えることができる
    class Point(object):
        pass
"""

"""
    今度はクラス固有の属性について考える。
    ・X座標を表す値
    ・Y座標を表す値
    これら二つは値を保存しておくので、Point クラスの個々のインスタンスが持つ変数のようなもの。
    このことから「インスタンス変数」と呼ぶ。
    また、これ以外に
    ・原点からの距離を調べる
    ・他の座標との距離を調べる
    これらの機能があると便利だと予想される。
    これらはインスタンスが持つ個々の値を利用して計算処理を行うので「インスタンスメソッド」と呼ぶ。
    クラスが持つ属性を「メンバ」と呼ぶ。
"""
point1.x = 1.0
point1.y = 1.0
print(dir(point1))
#<class '__main__.Point'>
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'y']
"""
    上記のようにすることで、point1 インスタンスに x, y 属性が新たに作成される。
    あくまで属性が追加されるのは point1 インスタンスのみ。
    クラスには追加されていないので、新しくインスタンスを生成してもそいつには x, y 属性がない。
    インスタンスを生成したときに同時に x, y 属性の値を設定できると便利だ。
    それをするのに、__init__ という名前のメソッドを用いる。
    __init__ メソッドはPython では特殊な扱いをされていて、インスタンスが生成される際に、そのインスタンスごとに固有の初期化処理を行うためにこのメソッドが自動的に呼び出されるようになっている。
    他の言語における、コンストラクタに似たもの。
    point = Point(1.0, 1.0)
    とすることで __init__ の引数に 1.0, 1.0 が渡される。
    クラス内で __init__ は、
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    のように定義され、self すなわち Point クラス自身の x 属性に x 引数を代入するようになる。

    def __init__(self[, param]):
        インスタンスの初期化を行う処理
    self 初期化処理を行うインスタンス。
    param 初期化に必要なデータを列挙する。

    関数とメソッドの違いとして、メソッドの第一引数は常に self となる。
    __init__ の場合、引数 self は __init__ 内部で初期化処理を行う対象となるインスタンスを指す。
    通常メソッドは インスタンス.メソッド（引数）で呼び出すが、__init__ メソッドでは、作成されたインスタンスが自動で self に代入されるので、メソッドを呼び出して self を明示する必要はない。

    第二引数以降はインスタンスの初期化に必要となるものを列挙していく。
    例えば、x 座標の値と y 座標の値の値が必要になる。
    __init__ は自動で呼び出される。どうやって __init__ の引数に値を渡すのかと言うと、クラスのインスタンス生成時に、クラスの引数にしたものが __init__ に渡されるようになっている。
    つまり
    point1 = Point(1.0, 1.0)
    とするなら、__init__ の引数も二つ設定する。
"""
class PointSecond:
    def __init__(self, x = 1.0, y = 1.0):
        self.x = x
        self.y = y
point2 = PointSecond(1.0, 1.0)
point3 = PointSecond()
"""
    self.x, self.y という表現。
    「初期化対象のインスタンスの属性 x」「初期化対象のインスタンスの属性 y」を意味している。
    point1.x = 1.0 とかいちいちやる必要がなくなる。
    尚、def __init__(self, x = 0.0, y = 0.0) とすることで、インスタンス生成時の引数を省略したときの x, y の値を設定できる。
    よって、point2.x, y は 1.0, 1.0 が代入され、point3.x, y は 0.0, 0.0 が代入される。
"""

#次に、二点間の距離を求める。
from math import sqrt
class PointDiff:
    def __init__(self, x = 1.0, y = 1.0):
        self.x = x
        self.y = y
    def diff(pt1, pt2):
        print(sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2))
point4 = PointDiff(4.0, 5.0)
point5 = PointDiff(2.7, 8.1)
PointDiff.diff(point4, point5)

"""
    あるクラスに属するオブジェクトが持つべきデータ（インスタンス変数）を明確にするには、__init__ メソッドでそれらを初期化することが肝心となる。
    Point クラスを例にとれば、そうすることで、その言うんスタンスが必ず属性 x を持つことが保証される。
    そうなれば、それらの属性を使った処理を安心して行えるようになる。
"""

class PointMaster:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def difference(self, point = None): #メソッドの第一パラメータは必ず self
        if not point:
            point = PointMaster() #原点を表すインスタンスを生成
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
"""
    point1.difference() とすれば self は point1 になる。
    つまり、メソッド呼び出しに使われる PointMaster クラスのインスタンスと、第二引数に渡された PointMaster クラスのインスタンスとの距離を算出することになる。
    
    第二引数には PointMaster クラスのインスタンスを渡すが、そのデフォルトが None に指定されているので、 difference メソッドを呼び出した癖に引数を指定しなかった時には、point 引数の値は None にされる。
    None は値が存在しないことを意味する。
    Python の特殊な組み込み定数で、プール演算を行う際には偽として扱われる。
    そこで、まずは if を用いて引数 point が偽かどうかを調べて、そうであれば原点を表す Point クラスのオブジェクトを作成することで最終的には二点間の距離を求める公式を使って戻り値を計算するようにしている。
    そうすることで原点からの距離と、二点間の距離の両者を一つのクラスで計算できるようにしている。

    尚、本プログラムでは、difference メソッドの返り値が二点間の距離になっている。
"""
point6 = PointMaster(4.5, 5.5)
point7 = PointMaster(3.2, 8.6)
print(str(point6.x) + ", " + str(point6.y))
print(str(point7.x) + ", " + str(point7.y))
print(point6.difference()) #point6 の原点からの距離を算出
print(point7.difference()) #point7 の原点からの距離を算出
print(point6.difference(point7)) #point6 と point7 の距離を算出
print(point7.difference(point6)) #point7 と point6 の距離を算出
#一番下の二つは値が同じになるはず。








