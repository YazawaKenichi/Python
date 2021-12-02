#jpg から png を作るプログラム
#複数処理

import cv2
import os
import glob # ワイルドカードを使用してファイルを取得したい
import time

def StartProcess():
    print("カレントディレクトリ及びサブディレクトリにある複数の jpg を png に変換します。")
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
#        time.sleep(0.05)
        i += 1
    j += 1

j = 0

filelist = glob.glob("*.jpg") + glob.glob("*.png")
print("filelist = ", filelist)
while(len(filelist) > j):
    image = cv2.imread(filelist[j])
    print(filelist[j] + "was imported.")
    cv2.imwrite(str(j) + ".png", image)
    print(filelist[j] + " was converted." + filelist[j] + " -> " + str(j) + ".png")
    j += 1

j = 0

while(len(directorylist) > j):
    filelist = glob.glob(directorylist[j] + "*.jpg")
    i = 0
    while(len(filelist) > i):
        print("os.remove(" + filelist[i] + ")")
        os.remove(filelist[i])
        i += 1
    j += 1

j = 0

filelist = glob.glob("*.jpg")
while(len(filelist) > j):
    print("os.remove(" + filelist[i] + ")")
    os.remove(filelist[j])
    j += 1

