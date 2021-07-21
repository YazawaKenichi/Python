#円弧を描画

import cv2


img = cv2.imread("1.jpg")
center = (190, 105) #中央の位置
axes = (20, 50) #(横方向半径, 縦方向半径) #楕円描画の時と違って今度は半径であることに注意
angle = 30 #x 軸を基準とする時計回り正方向の度数法回転量
startAngle = -60 #基準はちゃんと x 軸方向だと思われる
endAngle = -60 + 180
color = (255, 255, 255)
_thickness = 1
_lineType = cv2.LINE_AA
_shift = 0

cv2.imshow("src", img)
cv2.waitKey(0)

#円の描画
dst = cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness = _thickness, lineType = _lineType, shift = _shift)

cv2.imshow("Arc", dst)
cv2.waitKey(0)

"""
    楕円描画も円弧描画も ellipse メソッドを使う
    違いとしては引数がだいぶ違う

    楕円
    elipse の引数にある box の中に center, axes, angle
    axes の値は直径
    lineType = cv2.LINE_AA にしても shift 引数を設定できない

    円弧
    ellipse の引数に直接 center, axes, angle 
    axes の値は半径
    lineType = cv2.LINE_AA にすれば shift 引数を設定できる
"""
