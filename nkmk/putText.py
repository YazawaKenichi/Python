#文字列を描画

import cv2

img = cv2.imread("1.jpg")

#画像の大きさの取得し、テキストの中心をどこに置けばいいのか計算
height, width = img.shape[:2]
_x = 200 #文字列の横幅 (今のところ目測するしか方法を知らない)
_y = 50 #文字列の縦幅 (フォントスケールをいじると値が変わる)
x = round(width * 1/2 - _x * 1/2)
y = round(height * 7/8 + _y * 1/2)

text = "Hello, Yuika!" #表示したい文字列
org = (x, y) #文字列の左下座標
fontFace = cv2.FONT_HERSHEY_COMPLEX #フォントの設定
fontScale = 1.0 #フォントスケール（倍率）
color = (0, 0, 0)
_thickness = 1
_lineType = cv2.LINE_8

cv2.imshow("src", img)
cv2.waitKey(0)

#テキストの描画
dst = cv2.putText(img, text, org, fontFace, fontScale, color, thickness = _thickness, lineType = _lineType)

cv2.imshow("PutText", dst)
cv2.waitKey(0)
