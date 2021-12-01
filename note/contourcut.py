import cv2
import numpy as np

# Import Image
image = cv2.imread("sample.jpg")

# Encording to Grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# HSV Encording
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

# Generate Mask by Color Range
mask_image = cv2.inRange(hsv_image, np.array([159, 127, 0]), np.array([177, 255, 255]))

# Export Contours
contours, hierarchy = cv2.findContours(mask_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Remove small Contours as error
contours = list(filter(lambda x: cv2.contourArea(x) > 100, contours))

# Drawing Contours
cv2.drawContours(image, contours, -1, color = (0, 0, 255), thickness = 2)

# Display Image
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
    contours, hierarchy = cv2.findContours(image, mode, method[offset])
    引数
        image : 入力画像
        mode : 輪郭を検索する方法 輪郭をどのような階層構造で検索するかを指定する
        method : 輪郭を近似する方法 輪郭を近似する方法を指定する
        offset : 輪郭に加算するオフセット
    戻り値
        contours : 輪郭リスト
        hierarchy : 階層構造のリスト

    mode の種類
        cv2.RETR_EXTERNAL : 一番外側の輪郭のみ抽出
        cv2.RETR_LIST : すべての輪郭を抽出し、階層構造を作成しない
        cv2.RETR_CCOMP : すべての輪郭を抽出し、二階層の階層構造を作成
        cv2.RETR_TREE : すべての輪郭を抽出し、ツリーの階層構造を作成

    method の種類
        cv2.CHAIN_APPROX_NONE : 全ての輪郭を近似する
        cv2.CHAIN_APPROX_SIMPLE : 端点の輪郭のみ近似する（長方形の場合は角4点）
        cv2.CHAIN_APPROX_TC89_L1 : Teh-Chin approximationアルゴリズムの一つを適用
        cv2.CHAIN_APPROX_TC89_KCOS : Teh-Chin approximation アルゴリズムの一つを適用

    area = cv2counterArea(contour[, oriented])
    輪郭の面積を計算することができる
    引数
        contour : 輪郭
        oriented : 輪郭の方向
    戻り値
        area : 輪郭の面積

    len = cv2.arcLength(contour[, closed])
    輪郭の円周長を計算することができる
    引数
        contour : 輪郭
        closed : 輪郭が閉じているかどうか
    戻り値
        len : 輪郭の円周長

    approx = cv2.approxPolyDP(contour, epsilon, closed)
    輪郭を近似し、複雑な輪郭の超点数を減らすことができる
    引数
        contour : 輪郭
        epsilon : 実輪郭と近似輪郭の最大距離
        closed : 輪郭が閉じているかどうか
    戻り値
        approx : 輪郭の近似

    x, y, w, h = cv2.boundingRect()
    輪郭に外接する矩形を計算することができる
    引数
        contour : 輪郭
    戻り値
        x : 外形矩形の x 座標
        y : 外形矩形の y 座標
        w : 外形矩形の幅
        h : 外形矩形の高さ
"""

