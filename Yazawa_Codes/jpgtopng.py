#jpg から png を作るプログラム
#複数処理

import cv2
import os
import glob # ワイルドカードを使用してファイルを取得したい

def StartProcess():
    print("カレントディレクトリにある複数の jpg を png に変換します。")
    print("念のため png も更新します。")
    input("準備はよろしいですか？＞")

StartProcess()

filelist = glob.glob("*.jpg") + glob.glob("*.png")
print("filelist = ", filelist)
i = 0
while (len(filelist) > i):
    image = cv2.imread(filelist[i])
    print(filelist[i] + " was imported.")
    cv2.imwrite(str(i) + ".png", image)
    print(filelist[i] + " was converted. " + filelist[i] + " -> " + str(i) + ".png")
    os.remove(filelist[i])
    i += 1

