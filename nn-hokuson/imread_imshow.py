#画像の表示

#OpenCV モジュールをインポート
import cv2

#firstimg を作成（Mat 型変数）
firstimg = cv2.imread("1.jpg")

#ウィンドウでイメージファイルを表示
#ウィンドウの名称は First Image, 表示するイメージは firstimg
cv2.imshow("First Image", firstimg)

#キー入力を待つ
cv2.waitKey(0)
