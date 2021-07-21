#ヒストグラムの平滑化

import cv2

img = cv2.imread("1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#ヒストグラムの平滑化
dst = cv2.equalizeHist(gray)

cv2.imshow("src", img)
cv2.waitKey(0)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.imshow("EqualizeHist", dst)
cv2.waitKey(0)

"""
    ヒストグラムを均一化することで、コントラストを工場させたり、画像の全体的な明るさのバランスを改善することができる。
    均一化することで、ヒストグラムが左右に広がって平らになる。
"""
