# nn-hokuson の threshold.py と Yazawa_Codes の jpg to png を合わせて作った。

import cv2
import os

thresh = 140 #閾値
max = 300 #明度の最大値

def StartProcess():
    print("複数の jpg を png に変換し、二値画像にします。")
    print("ファイル名一括編集ソフト等を用いて、変換したいファイルの名称を連番にしてください。")
    print("png が混ざっている場合は png を二値化します。")
    print("カレントディレクトリに encorded ディレクトリを作成し、そこに変換した後のファイルを出力します。")
    input("準備はよろしいですか？＞")

i = 0

StartProcess()

os.mkdir("./converted")

while 1:
    i += 1
    jpg_name = str(i) + ".jpg"
    png_name = str(i) + ".png"
    jpg = cv2.imread(jpg_name)
    png = cv2.imread(png_name)
    if(not jpg is None):
        print(str(i) + ".jpg was imported.")
        # 一度グレイスケールにする
        jpg = cv2.cvtColor(jpg, cv2.COLOR_RGB2GRAY)
        # グレイスケールしたものを二値化する
        retval, jpg = cv2.threshold(jpg, thresh, max, cv2.THRESH_BINARY)
        print(str(i) + ".jpg was converted.")
        cv2.imwrite("./converted/" + png_name, jpg)
    elif(not png is None):
        print(str(i) + ".png was imported.")
        png = cv2.cvtColor(png, cv2.COLOR_RGB2GRAY)
        retval, png = cv2.threshold(png, thresh, max, cv2.THRESH_BINARY)
        print(str(i) + ".png was converted.")
        cv2.imwrite("./converted/" + png_name, png)
    else:
        print("End this program.")
        break

