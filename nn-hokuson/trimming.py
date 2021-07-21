#トリミング

import cv2

img = cv2.imread("3.jpg")

#
cv2.imshow("Source", img)
offset_x = 0
offset_y = 100
size = 200
"""
    offset_x, offset_y, size
    イラストレータの三峰：130 ~ 150, 130 ~ 150, 200
    シャニの三峰：240, 0, 200
    鮭：0, 0, 200 #にして下の # を入れ替える
"""


img_trim = img[offset_y : offset_y + size, offset_x : offset_x + size]
#img_trim = img[-size : , offset_x : offset_x + size] #鮭の場合はこちらを選択
cv2.imshow("Trimming", img_trim)
cv2.waitKey(0)

"""
    トリミングは新しく関数を使う必要がないみたい
    cv2
    Mat imread(str filename)
    で定義されることから、Mat 型は画像のピクセルレベルの色彩情報を配列化して格納している様子が伺える。
    しかも Mat img[ Y 座標, X 座標] の順番かよ、わかりにく。
"""
