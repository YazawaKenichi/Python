#図形の描画

import cv2

img = cv2.imread("1.jpg")
pt1 = (50, 10)
pt2 = (125, 10)
color = (0, 255, 255)
_thickness = 4
_lineType = cv2.LINE_AA
_shift = 0

cv2.imshow("src", img)
cv2.waitKey(0)

#直線を引く
dst = cv2.line(img, pt1, pt2, color, thickness = _thickness, lineType = _lineType , shift = _shift)

cv2.imshow("?", img)
cv2.waitKey(0)

cv2.imshow("line", dst)
cv2.waitKey(0)

"""
    Mat cv2.line(img, pt1, pt2, color, thickness = 1, lineType = cv2.LINE_8, shift = 0)

    返り値が Mat 型で、直線を描画した後の図を格納してくれる
    ただ img にも同時に格納されるっぽいので返り値を利用する必要は無さそう
    それよりも直前の行で
    dst = img
    とかやってバックアップ？しておくと良いかも

    img
    描画したい地の画像
    
    pt1
    線の始点
    
    pt2
    線の終点
    
    color
    色。BGR の順に指定
    
    thickness
    線の太さ、内部の塗りつぶし
    単位はピクセル
    枠線の色と塗りつぶしの色を別々にするには、塗りつぶし図形を描画してから、同じ位置にさらに枠線を描画する必要がある。
    一度に指定することはできない。

    lineType
    線を描画するアルゴリズムの種類
    以下その種類
    cv2.LINE_4：四連結
    cv2.LINE_8：八連結（デフォ）
    cv2.LINE_AA：アンチエイリアス

    shift
    座標の小数部分のビット数を整数で指定する。
    アンチエイリアス前提の機能なので、lineType は cv2.LINE_AA を指定する必要がある。
    ゼロがデフォ
    shift を指定すると、座標が (x * 2^(-shift), y * 2^(-shift)) として計算される。

"""
