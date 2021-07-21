#円を描画

import cv2

img = cv2.imread("1.jpg")
center = (190, 35)
radius = 15
color = (255, 255, 255)
_thickness = -1 #負で塗りつぶし
_lineType = cv2.LINE_AA
_shift = 0

cv2.imshow("src", img)
cv2.waitKey(0)

#円の描画
dst = cv2.circle(img, center, radius, color, thickness = _thickness, lineType = _lineType, shift = _shift)

cv2.imshow("circle", dst)
cv2.waitKey(0)
