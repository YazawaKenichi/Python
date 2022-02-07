#矢印の描画

from pathlib import Path
import cv2

filename = input("Enter filename : ")

img = cv2.imread(filename) #描画したい画像
x = int(1920 / 2) - 50 - 100
dx = 80
y = int(1080 / 3) - 50 - 10
_thickness = 25 #線の太さ、内部の塗りつぶし
_shift = 0 #座標の小数部分のビット数
_tipLength = 0.1 #屋の先の部分の長さ

pt1 = (x - dx, y) #始点
pt2 = (x + dx, y) #終点
color = (0, 0, 0) #色
dst1 = cv2.line(img, pt1, pt2, color, thickness=_thickness, lineType=cv2.LINE_8, shift=_shift)

x = x / 3 - 60
pt1 = (int(x - dx), y)
pt2 = (int(x + dx), y)
color = (0, 0, 0) #色
dst2 = cv2.line(dst1, pt1, pt2, color, thickness=_thickness, lineType=cv2.LINE_8, shift=_shift)

x = x * 3 * 2.5 - 160
pt1 = (int(x - dx), y)
pt2 = (int(x + dx), y)
color = (0, 0, 0) #色
dst3 = cv2.line(dst2, pt1, pt2, color, thickness=_thickness, lineType=cv2.LINE_8, shift=_shift)

cv2.imwrite(str(Path(filename).stem) + "_namemosaiced.png", dst3)
cv2.waitKey(0)

# Reference
# https://techacademy.jp/magazine/22729#:~:text=Python%E3%81%A7%E6%A8%99%E6%BA%96%E5%85%A5%E5%8A%9B%E3%82%92,%E3%81%8C%E6%A8%99%E6%BA%96%E5%87%BA%E5%8A%9B%E3%81%A8%E3%81%AA%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82    # Python で標準入力を受け付ける。
# https://note.nkmk.me/python-opencv-draw-function/ # OpenCV を用いて直線を描画する。
# https://note.nkmk.me/python-opencv-imread-imwrite # 画像をファイルに保存。/
# https://www.delftstack.com/ja/howto/python/python-get-filename-without-extension-from-path/#:~:text=%E5%8F%96%E5%BE%97%E3%81%97%E3%81%BE%E3%81%99%E3%80%82-,Python%20%E3%81%AE%20pathlib.path().stem%20%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6,%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%90%8D%E3%82%92%E8%BF%94%E3%81%97%E3%81%BE%E3%81%99%E3%80%8u   # Python パスから拡張子無しのファイル名を取得する。









