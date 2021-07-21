#楕円を描画

import cv2

center = (190, 105) #中央の位置
axes = (20, 50) #(横方向直径, 縦方向直径)
angle = 30 #x 軸を基準とする時計回り正方向の度数法回転量

img = cv2.imread("1.jpg")
box = (center, axes, angle)
color = (255, 255, 255)
_thickness = 1 #負で塗りつぶし
_lineType = cv2.LINE_8

cv2.imshow("src", img)
cv2.waitKey(0)

#円の描画
dst = cv2.ellipse(img, box, color, thickness = _thickness, lineType = _lineType)

cv2.imshow("Ellipse", dst)
cv2.waitKey(0)
