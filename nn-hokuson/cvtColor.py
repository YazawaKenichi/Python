#グレイスケール変換

import cv2

src = cv2.imread("1.jpg")

#色空間を変換する関数 cvtColor()
dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

cv2.imshow("Gray_Scale", dst)
cv2.waitKey(0)

#以下を実行すると 1.jpg のファイル自体がグレイスケールにされるので注意
'''
cv2.imwrite("1.jpg", cv2.cvtColor(cv2.imread("1.jpg"), cv2.COLOR_BGR2GRAY))
cv2.waitKey(0)
'''

"""
    参考：https://water2litter.net/rum/post/python_cv2_grayscale/
    
    cvtColor() メソッド

    dst = cv2.cvtColor(src, code)
    
    変数 dst
    numpy.ndarray 型
    変換後のイメージを格納

    変数 src
    numpy.ndarray 型
    変換前のイメージを格納

    変数 code
    列挙型
    変換内容を示す列挙型の値

    何から何に変換するかは code のところで指定する
    いくつか種類がある
    種類については参照：https://docs.opencv.org/3.3.0/d7/d1b/group__imgproc__misc.html#ga4e0972be5de079fed4e3a10e24ef5ef0
"""
