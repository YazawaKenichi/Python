#jpg から png を作るプログラム
#複数処理

import cv2
import os

png_mode = True

def StartProcess():
    print("複数の jpg を png に変換します。")
    print("webp が取り込まれた場合はそのファイルも png に変換します。")
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
    webp_name = str(i) + ".webp"
    jpg = cv2.imread(jpg_name)
    png = cv2.imread(png_name)
    webp = cv2.imread(webp_name)
    if (not jpg is None):
        print(str(i) + ".jpg was imported.")
        cv2.imwrite(png_name, jpg)
        print(str(i) + ".jpg was converted.")
        os.remove(jpg_name)
    elif (not png is None):
        print(str(i) + ".png was imported.")
        cv2.imwrite(png_name, png)
        print(str(i) + ".png was converted.")
    elif (not webp is None):
        print(str(i) + ".webp was imported.")
        cv2.imwrite(png_name, webp)
        print(str(i) + ".webp was converted.")
        os.remove(jpg_name)
    else:
        input("End this Program.")
        break

