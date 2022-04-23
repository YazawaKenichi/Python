#jpg から png を作るプログラム
#複数処理

import cv2
import os
import glob # ワイルドカードを使用してファイルを取得したい

def StartProcess():
    print("Menu")
    print("1.jpg")
    print("2.webp")
    print("4.png")
    mode = int(input(" > "))
#    print("カレントディレクトリにある複数の jpg を png に変換します。")
#    print("念のため png も更新します。")
#    input("準備はよろしいですか？＞")

def getjpg()
    return glob.glob("*.jpg") + glob.glob("*jpeg") + glob.glob("*.jfif")

def getwebp()
    return glob.glob("*.webp")

def getpng()
    return glob.glob("*.png") + glob.glob("*.ping")

StartProcess()

if mode == 1
    filelist = getjpg()
if mode == 2
    filelist = getwebp()
if mode == 3
    filelist = getjpg() + getwebp()
if mode == 4
    filelist = getpng()
if mode == 5
    filelist = getjpg() + getpng()
if mode == 6
    filelist = getwebp() + getpng()
if mode == 7
    filelist = getjpg() + getwebp() + getpng()

print("filelist = ", filelist)
i = 0
while (len(filelist) > i):
    image = cv2.imread(filelist[i])
    print(filelist[i] + " was imported.")
    cv2.imwrite(str(i) + ".png", image)
    print(filelist[i] + " was converted. " + filelist[i] + " -> " + str(i) + ".png")
    os.remove(filelist[i])
    i += 1

