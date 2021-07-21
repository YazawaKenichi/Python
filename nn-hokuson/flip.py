#画面の胸像異性体

import cv2

img = cv2.imread("1.jpg")

x = cv2.flip(img, 0) #x 軸に対して線対称（上下反転）
y = cv2.flip(img, 1) #y 軸に対して線対称（左右反転）
xy = cv2.flip(img, -1) #原点に対して点対称（上下左右反転）

cv2.imshow("src", img)
cv2.waitKey(0)
cv2.imshow("X-Flip", x)
cv2.waitKey(0)
cv2.imshow("Y-Flip", y)
cv2.waitKey(0)
cv2.imshow("XY-Flip", xy)
cv2.waitKey(0)

"""
    Mat cv2.flip(Mat img, int axis)
    axis >= 0 : Y 軸対称・左右反転
    axis == 0 : X 軸対称・上下反転
    axis <= 0 : 原点対称・上下左右反転
"""
