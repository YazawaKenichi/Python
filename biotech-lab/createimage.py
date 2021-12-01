import cv2
import numpy as np

blackimage = np.zeros((200, 300), np.uint8) # 200 x 300 のグレイスケール画像を新規作成

"""
OpenCV-Python において、画像は numpy.ndarray として扱われるので、新規イメージを作成するには、単純に numpy.ndarray の配列を作成するだけ。
黒のピクセルの画素値はゼロなので、numpy.zeros 関数を用いて、要素が全てゼロの numpy.ndarray 配列を作成する。
np.uint8 というのはデータ型。
OpenCV に於いて画素値の範囲は 256 段階なので 8 ビットで表現できる。
uint8 を指定しないデフォルトのままだと float になる。
... float でどうやって画素値指定すんだ？？？？
"""

# 同様にして白のグレイスケール画像は以下のようにする

whiteimage = np.ones((200, 300), np.uint8) * 255

"""
白のピクセル画素値は 255 なので、numpy.one 関数を用いて、要素が全てイチの numpy.ndarray 配列を作成し、それを 255 倍にする。
"""

# 画像の保存
cv2.imwrite("./blackimage.png", blackimage)
cv2.imwrite("./whiteimage.png", whiteimage)

"""
cv2.imwrite() メソッドを用いることで nparray イメージを保存することができる。
"""

# カラー画像の作成
redimage = np.zeros((200, 300, 3), np.uint8)
redimage[:, :, 2] = 255 # H, W, GBR のうち、全ての R を 255 にする
cv2.imwrite("./redimage.png", redimage)

cv2.imshow("BlackImage", blackimage)
cv2.waitKey(0)

cv2.imshow("WhiteImage", whiteimage)
cv2.waitKey(0)

cv2.imshow("RedImage", redimage)
cv2.waitKey(0)

cv2.destroyAllWindows()

"""
このコードを読んで分かったこと
np.zeros 及び np.ones の第一引数について
(高さ、横幅、色の数) で指定する。
高さと横幅についてはそのままピクセルの値を入れる。
色の数については、何も指定しないことでデフォルトの白黒画像（グレイスケール）が表現できる。
3 を指定することで GRB の三色カラーコードを指定できるようになる。
これらの値をリスト型で関数に渡すと、そのしていしたサイズの nparray 配列が用意される。

nparray 配列の扱いについて（復習）参考：https://note.nkmk.me/python-numpy-ndarray-slice/
とりあえずこの画像がわかりやすい
https://qiita-user-contents.imgix.net/https%3A%2F%2Fgithub.com%2Ftanuk1647%2Fenjoy-slice-life%2Fraw%2Fmaster%2Ffigures%2Fenjoy-slice-life-0001.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=b41fdc951324c38925afa8732b692bf3
始点または終点を省略するとシーケンスの先頭から取得と末尾から取得ができる。
カンマで区切ることによって、次元ごとにスライスすることができる。
一次元目：縦幅
二次元目：横幅
三次元目：GBR
"""

