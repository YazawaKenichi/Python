from tkinter import *
from tkinter import ttk

root = Tk()
root.title('My First App')

#ヴィジェットの作成
frame1 = ttk.Frame(root, padding = 16)
label1 = ttk.Label(frame1, text = 'Your Name:')
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable = t)
button1 = ttk.Button(frame1, text = 'OK', command = lambda: print('Hello, %s.' % t.get()))

#レイアウト
frame1.pack()
label1.pack(side = LEFT)
entry1.pack(side = LEFT)
button1.pack(side = LEFT)

#ウィンドウの表示開始
root.mainloop()

"""
	Tk() の呼び出しでルート要素を作成。
	ルート要素はベースとなるウィンドウそのものを表す。
	Tk クラスの root インスタンスを生成。

	root インスタンスの title メソッドの引数に文字列を指定。
	ルートのウィンドウにタイトルを設定できる。
	
	
"""

