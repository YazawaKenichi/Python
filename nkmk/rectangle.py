#長方形を描画

import cv2

img = cv2.imread("1.jpg")
pt1 = (50, 150)
pt2 = (125, 200)
color = (255, 255, 0)
_thickness = 1
_lineType = cv2.LINE_8
_shift = 0

cv2.imshow("src", img)
cv2.waitKey(0)

#長方形の描画
dst = cv2.rectangle(img, pt1, pt2, color, thickness = _thickness, lineType = _lineType, shift = _shift)

#img に直接長方形が描画されているのは省略

cv2.imshow("Rectangle", dst)
cv2.waitKey(0)
