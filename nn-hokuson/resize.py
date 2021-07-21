import cv2

src = cv2.imread("1.jpg")

width = 200
height = 200
dst = cv2.resize(src, dsize = (width, height)) #指定サイズでリサイズ
cv2.imshow("cv2.resize(src, dsize = (200, 200))", dst)
cv2.waitKey(0)

width = 0.5
height = 0.5
dst = cv2.resize(src, dsize = None, fx = width, fy = height) #指定倍率でリサイズ
cv2.imshow("cv2.resize(src, dsize = None, fx = 0.5, fy = 0.5)", dst)
cv2.waitKey(0)

width = 250 #単位ピクセル
h, w = src.shape[:2] #画像の縦横のピクセルを取得
height = round(width * h/w) #指定した横幅ピクセルから縦幅ピクセルを計算する
dst = cv2.resize(src, dsize = (width, height))
cv2.imshow("cv2.resize(src, dsize = (250, auto))", dst)
cv2.waitKey(0)

height = 250 #単位ピクセル
h, w = src.shape[:2] #画像の縦横のピクセルを取得
width = round(height * w/h) #指定した縦幅ピクセルから横幅ピクセルを計算する
dst = cv2.resize(src, dsize = (width, height))
cv2.imshow("cv2.resize(src, dsize = (auto, 250))", dst)
cv2.waitKey(0)

'''
    リサイズ
    dst = cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    
    src
    入力画像
    デフォルトで ndarray.None

    dsize
    リサイズ後の大きさを (w, h) で指定
    デフォルトで tuple of 2-ints
    fx, fy でリサイズの大きさを指定する場合は dsize = None にする

    fx
    float型
    x 方向の倍率を決める
    デフォルトでゼロ

    fy
    float型
    y 方向の倍率を決める
    デフォルトでゼロ

    interpolation
    ndarray 型
    補間方法
    デフォルトで cv2.INTER_LINEAR
    以下種類
    cv2.INTER_NEAREST：最近傍補間
    cv2.INTER_LINEAR：バイリニア補間
    cv2.INTER_CUBIC：バイキュービック補間
    cv2.INTER_AREA：ピクセル領域の関係を利用したサンプリング
    cv2.INTER_LANCZOS4：Lanczos 補間

    dst
    リサイズ後の画像
'''
