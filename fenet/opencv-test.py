#OpenCV モジュールを import
import cv2

#1imread インスタンスを作成
testimg = cv2.imread("testimg.jpg")

#testimg をウィンドウで表示
cv2.imshow("", testimg)

#以下二行はよくわからん
cv2.waitKey(0)
cv2.destroyAllWindows()

