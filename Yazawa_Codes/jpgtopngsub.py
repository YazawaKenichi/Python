#jpg から png を作るプログラム
#複数処理

import cv2
import os
import glob # ワイルドカードを使用してファイルを取得したい
import time

def StartProcess():
    print("複数のサブディレクトリにある複数の jpg を png に変換します。")
    print("念のため png も更新します。")
    input("準備はよろしいですか？＞")

j = 0

StartProcess()

directorylist = glob.glob("*/")
print("directorylist = ", directorylist)
while(len(directorylist) > j):
    filelist = glob.glob(directorylist[j] + "*.jpg") + glob.glob(directorylist[j] + "*.png")
    print("directorylist[" + str(j) + "] = ", directorylist[j])
    print("filelist = ", filelist)
    i = 0
    while (len(filelist) > i):
        image = cv2.imread(filelist[i])
        print(filelist[i] + " was imported.")
        cv2.imwrite(directorylist[j] + str(i) + ".png", image)
        print(filelist[i] + " was converted. " + filelist[i] + " -> " + directorylist[j] +  str(i) + ".png")
#        time.sleep(0.05)    # これがないと処理が早すぎて CPU に負担がかかる
        os.remove(filelist[i])
#        time.sleep(0.05)
        i += 1
    j += 1

# https://www.javadrive.jp/python/list/index5.html  # リストの長さの取得
# https://atmarkit.itmedia.co.jp/ait/articles/1905/31/news015.html  # リストの操作
# https://techacademy.jp/magazine/41694 # ワイルドカードの使用方法

