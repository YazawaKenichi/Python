#マーカーを描画

import cv2

img = cv2.imread("1.jpg")
position = (375, 200) #座標の決定
color = (0, 255, 255)
_markerType = cv2.MARKER_STAR #マーカーの種類（十字や四角や三角など）
_markerSize = 50 #マーカーの大きさを指定できる
_thickness = 3 #負で塗りつぶし

cv2.imshow("src", img)
cv2.waitKey(0)

#円の描画
dst = cv2.drawMarker(img, position, color, markerType = _markerType, markerSize = _markerSize, thickness = _thickness)

cv2.imshow("DrawMarker", dst)
cv2.waitKey(0)

"""
    以下 markerType の種類
    MARKER_CROSS：十字
    MARKER_TILTED_CROSS：バツ印
    MARKER_STAR：アスタリスク
    MARKER_DIAMOND：ダイヤ
    MARKER_SQUARE：四角
    MARKER_TRIANGLE_UP：三角△
    MARKER_TRIANGLE_DOWN：三角▽
"""
