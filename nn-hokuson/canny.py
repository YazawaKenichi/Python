#輪郭検出

import cv2

low = 100 #小さい閾値
high = 150 #大きい閾値

img = cv2.imread("1.jpg")

cv2.imshow("src", img)
cv2.waitKey(0)

"""
#一旦カラーのまま出力してみる
tmp = cv2.Canny(img, low, high)
cv2.waitKey(0)
"""

#一旦モノクロ化
gray = cv2.cvtColor(img, cv2.THRESH_BINARY)

#輪郭検出
dst = cv2.Canny(gray, low, high)

cv2.imshow("Canny", dst)
cv2.waitKey(0)

"""
    Mat dist cv2.Canny(Mat src, int low, int high)
    輝度差（勾配）を境界として表示する（または判定する）ために、大きい閾値と小さい閾値を使用する。
    それが small と big
    輝度差が大きい閾値よりも大きい場合は境界線として認識する。
    Canny は「 high よりも輝度差が大きい場合」と「ヒステリシス閾値内の輝度差であっても隣のピクセルの輝度差が大きい場合」にそのピクセルを境界線として判定する。

    新用語
    ヒステリシス閾値：high と low の間の領域の事。

    例）high = 100, low = 30 と仮定する。
    あるピクセルの勾配が 70 であり、隣のピクセルの勾配が 100 を超えている場合、前者のあるピクセルは境界線となる。
    しかし隣のピクセルの勾配が 100 を下回っている場合、前者のあるピクセルは境界線にならない。
"""

