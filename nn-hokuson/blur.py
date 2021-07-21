#ぼかしフィルタ

import cv2

img = cv2.imread("1.jpg")

cv2.imshow("src", img)
cv2.waitKey(0)

#全体的にぼかす
dst1 = cv2.blur(img, (10, 10))
#（x 軸方向ぼかし, y 方向ぼかし）

cv2.imshow("Blur", dst1)
cv2.waitKey(0)

"""
#ガウスぼかし（中心ほどぼける）（以下ののどこかでエラーしてる）
sigma = 2 #ガウス関数の σ
dst2_tmp = cv2.GaussianBlur(img, (10, 10), sigma)
""""""sigma が大きいと中心がめっちゃぼける代わりに、ぼけの広がりが狭くなる""""""
""""""ガウス関数：y = exp(-x^2 / (2*sigma^2)) / square(2 * pi * sigma^2)""""""
dst2 = cv2.hconcat([img, dst2_tmp]) #なにしてんの？

cv2.imshow("Blur", dst2)
cv2.waitKey(0)
"""

"""
#中央値でぼかす（もう何やってるかわからん）（以下のどこかでエラーしてる）
dst3_tmp = cv2.medianBlur(img, 10)
dst3 = cv2.hconcat([img, dst3_tmp])

cv2.imshow("Blur", dst1)
cv2.waitKey(0)
"""
