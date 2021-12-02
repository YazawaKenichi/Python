# nn-hokuson の threshold.py と Yazawa_Codes の jpg to png を合わせて作った。

import cv2
import os
import glob

thresh = 140 #閾値
max = 300 #明度の最大値

def StartProcess():
    print("複数の画像を二値画像にし、さらに jpg は png に変換します。")
    print("カレントディレクトリに converted ディレクトリを作成し、そこに変換した後のファイルを出力します。")
    input("準備はよろしいですか？＞")

i = 0

StartProcess()

os.mkdir("./converted")
filelist = glob.glob("*.jpg") + glob.glob("*.png")

while(len(filelist) > i):
    src = cv2.imread(filelist[i])
    print(filelist[i] + " was imported.")
    # 一度グレイスケールにする
    img = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    # グレイスケールしたものを二値化する
    retval, img = cv2.threshold(img, thresh, max, cv2.THRESH_BINARY)
    print(filelist[i] + " was converted.")
    cv2.imwrite("./converted/" + str(i) + ".png", img)
    i += 1

