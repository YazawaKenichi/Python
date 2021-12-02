"""
	Special Thanks!
	https://qiita.com/East_san/items/8f4938967a605cecd2ef
"""

"""		import		"""

import cv2

"""		priparation		"""

filepass = input("加工したい画像のパスを入力してください。")
source_image = cv2.imread(filepass)

"""
SOURCE_IMAGE_WIDTH = ndarray.shape[0]	# インポートした画像の大きさをあらかじめ計算しておく
SOURCE_IMAGE_HEIGHT = ndarray.shape[1]
SOURCE_IMAGE_SIZE = os.path.getsize	# ファイルサイズの取得
"""

"""		define		"""

def myinput():	# 入力をさせる関数
	try:	# 例外の起こる可能性が高い処理
		inputnow = input(">")
	except:	# 例外が発生した場合、再帰する
		return inputmyinput()
	return inputnow

def input_mode():	# 0 ~ 7 を読み取って判断する。
	mode = int(myinput())
	if(mode > 0 and 7 > mode)
		return mode	# 入力された mode の値を返す。
	else
		return mode_select()	# 範囲外を指定した場合は再帰

def mode_select():	# モードの選択肢を表示してモードを入力させて入力した値を返す。
	print("1.四角で囲んでトリミング")
	print("2.横のピクセルを指定してリサイズ")
	print("3.縦のピクセルを指定してリサイズ")
	print("4.縦横のピクセルを指定してリサイズ")
	print("5.容量を指定してリサイズ")
	print("6.容量を指定して正方形にトリミング")
	print("")
	print("モードを選んでください。>")
	return input_mode()

def branch(mode):	# 選択されたモードによって呼び出す関数を変える
	if(mode == 1):
		rect_trim()
	if(mode == 2):
		w_pixelresize()
	if(mode == 3):
		h_pixelresize()
	if(mode == 4):
		hw_pixelresize()
	if(mode == 5):
		size_pixelresize()
	if(mode == 6):
		size_pixeltrim()

def rect_trim():
	# 四角で囲んでトリミングするプログラム	# 需要高め

def w_pixelresize():
	# 幅を指定してリサイズ	# 需要普通

def h_pixelresize():
	# 高さを指定してリサイズ	# 需要低め

def hw_pixelresize():
	# 幅と高さを指定してリサイズ	# 需要低め

def size_pixelresize():
	# 需要高め

def size_pixeltrim():
	# 需要高め

"""
	必要な処理
	モード毎に関数を作成する。この時、モードをまたいで共通する処理を関数化する。
"""

"""			main		"""

while(1)
{
	mode = mode_select()
	#mode の値によって実行する関数を変更する ifelif
}


