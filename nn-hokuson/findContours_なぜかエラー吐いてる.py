#輪郭の検出

import cv2

image = cv2.imread("1.jpg")
mode = cv2.RETR_FLOODFILL
method = cv2.CHAIN_APPROX_SIMPLE

image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
retval, image_Contours = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#輪郭の検出
image_return, contours, hierarchy = cv2.findContours(image, mode, method)

#すべての輪郭を読み込んで出力
tmp = image.copy()
cv2.drawContours(tmp, contours, -1, (0, 255, 0), 2)
cv2.imwrite("cv2.drawContours(image, mode, method).png", tmp)

"""
    contours, hierarchy = cv2.findContours(image, mode, method) メソッド

    list contours
    検出した輪郭のリスト。

    ndarray hierarchy
    検出した輪郭の階層情報。

    mode に指定できるもの
    RETR_EXTERNAL：一番外側の輪郭を出力する。
    RETR_LIST：すべての輪郭を出力する。
    RETR_CCOMP：すべての輪郭を２レベルの階層に分けて出力する。
    RETR_TREE：すべての輪郭を全体の階層構造で出力する。
    RETR_FLOODFILL：解説無し

    method に指定できるもの
    CHAIN_APPROX_NONE：輪郭の出力に、すべての検出点を含める。
    CHAIN_APPROX_SIMPLE：輪郭を出力するときに、省略できる検出点は省略する。
    CHAIN_APPROX_TC89_L1：解説無し
    CHAIN_APPROX_TC89_KCOS：解説無し
"""

"""
    cv2.drawContours(image, contours, contourIdx, color, [thickness], [lineType])

    ndarray image
    輪郭を書き込む画像のデータ

    list contours
    輪郭のリスト

    int contourIdx
    輪郭のインデックス
    -1 ですべての輪郭を表す
    最後から三文字目は大文字のアイ

    tuple color
    輪郭線の色。

    int thickness
    輪郭線の太さ。
    既定値１。
    省略可能。

    lineType
    輪郭線の線の種類。
    既定値は LINE_8
    省略可能。
"""
