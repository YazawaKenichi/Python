#jpg から png を作るプログラム
#複数処理

import cv2
import os

png_mode = True

def StartProcess():
    print("複数の jpg を png に変換します。")
    print("ファイル名一括編集ソフト等を用いて、変換したいファイルの名称を連番にしてください。")
    if png_mode:
        print("念のため png も更新します。")
    elif not png_mode:
        print("png が混ざっている場合は png が無視して処理されます。")
    input("準備はよろしいですか？＞")

i = 0

StartProcess()

while 1:
    i += 1
    jpg_name = str(i) + ".jpg"
    png_name = str(i) + ".png"
    jpg = cv2.imread(jpg_name)
    png = cv2.imread(png_name)
    if (not jpg is None):
        print(str(i) + ".jpg was imported.")
        cv2.imwrite(png_name, jpg)
        print(str(i) + ".jpg was converted.")
        os.remove(jpg_name)
    elif (not png is None):
        print(str(i) + ".png was imported.")
        cv2.imwrite(png_name, png)
        print(str(i) + ".png was converted.")
    else:
        print("End this program.")
        break

