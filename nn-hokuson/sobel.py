#輪郭検出

import cv2

img = cv2.imread("1.jpg")
bit = cv2.CV_32F #出力画像のビット深度
dx = 1 #x 方向微分の次数（１で横方向の輪郭を検出）
dy = 1 #y 方向微分の次数（１で縦方向の輪郭を検出）
_ksize = 3 #カーネルサイズ（-1 ~ 7 までの奇数しか指定できないらしい）

cv2.imshow("src", img)
cv2.waitKey(0)

#Sobel フィルタをかける
dst = cv2.Sobel(img, bit, dx, dy, ksize = _ksize)

cv2.imshow("Sobel", dst)
cv2.waitKey(0)

thresh = 175
max = 256
_ksize = 3
src = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
retval, thresholded = cv2.threshold(src, thresh, max, cv2.THRESH_BINARY)
result = cv2.Sobel(thresholded, bit, dx, dy, ksize = _ksize)
cv2.imshow("Threshold", thresholded)
cv2.waitKey(0)
cv2.imshow("Result", result)
cv2.waitKey(0)

"""
#以下実験コード
test_1 = cv2.Sobel(img, bit, dx, dy, ksize = 1)
cv2.imshow("Sobel ksize = 1", test_1)
cv2.waitKey(0)
test_3 = cv2.Sobel(img, bit, dx, dy, ksize = 3)
cv2.imshow("Sobel ksize = 3", test_3)
cv2.waitKey(0)
test_5 = cv2.Sobel(img, bit, dx, dy, ksize = 5)
cv2.imshow("Sobel ksize = 5", test_5)
cv2.waitKey(0)
test_7 = cv2.Sobel(img, bit, dx, dy, ksize = 7)
cv2.imshow("Sobel ksize = 7", test_7)
cv2.waitKey(0)

#ぶっちゃけ 1 と 3 の違いがわからん

cv2.imshow("Sobel ksize = 3 - 1", test_3 - test_1)
cv2.waitKey(0)
#一緒やんwww

cv2.imshow("Sobel ksize = 7 - 1", test_7 - test_1)
cv2.waitKey(0)
#これはこれで 7 と何が違うんだ？？？
"""