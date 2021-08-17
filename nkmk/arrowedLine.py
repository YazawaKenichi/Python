#矢印の描画

import cv2

img = cv2.imread("1.jpg") #描画したい画像
pt1 = (50, 130) #始点
pt2 = (125, 80) #終点
color = (255, 0, 255) #色
_thickness = 1 #線の太さ、内部の塗りつぶし
_shift = 0 #座標の小数部分のビット数
_tipLength = 0.1 #屋の先の部分の長さ

cv2.imshow("src", img)
cv2.waitKey(0)

#矢印を描画
dst = cv2.arrowedLine(img, pt1, pt2, color, thickness = _thickness, shift = _shift, tipLength = _tipLength)

cv2.imshow("?", img) #やはり img にも矢印が追加されている様子。OpenCV で描画するときはいつでも返り値を代入必要はないのかもしれない。ただ慣れないので返り値代入法でやっていきたい
cv2.waitKey(0)

cv2.imshow("cv2.arrowedLine", dst)
cv2.waitKey(0)

