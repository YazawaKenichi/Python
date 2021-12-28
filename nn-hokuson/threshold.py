import cv2

thresh = 140 #閾値
max = 300 #明度の最大値

original = cv2.imread("4.jpg")

src = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)

#二値化 
retval, dst = cv2.threshold(src, thresh, max, cv2.THRESH_BINARY)
#二値化する前にグレイスケールに変換して、それを二値化する必要があるっぽい
#cv2.threshold() の返り値は二つあるみたい
#retval は cv2.THRESH_OTSU か cv2.THRESH_TRIANGLE を使用したときに自動的に決まった閾値を格納する。
#dst は二値画像を格納する。
#返り値が二つは必要で、retval は使うときと使わない時があるという事か。

cv2.imshow("Threshold", dst) #文字化けするんだが？
cv2.waitKey(0)

