#折れ線・多角形を描画

import cv2
import numpy as np

img = cv2.imread("1.jpg")
pts = np.array(((300, 80), (300, 130), (335, 130))) #各点の座標を示す
isClosed = False #始点と終点を結ぶか否か
color = (0, 255, 255)
_thickness = 3 #負で塗りつぶし
_lineType = cv2.LINE_AA
_shift = 0

cv2.imshow("src", img)
cv2.waitKey(0)

#円の描画
dst = cv2.polylines(img, pts, isClosed, color, thickness = _thickness, lineType = _lineType, shift = _shift)

cv2.imshow("PolyLines", dst)
cv2.waitKey(0)

"""
    pts には各点の座標を示す NumPy 配列（二次元配列）のリストや配列を指定する。
    複数の折れ線を一度に描画できる。
    折れ線が一つの場合も[]で囲むなどしてリストにする必要がある。
    尚、三次元配列でも可能。
"""

