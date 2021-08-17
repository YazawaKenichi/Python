"""
	tkinter は Python の標準的な GUI ツール。
	他の GUI ツールと比べて
	１．動作が安定している
	２．起動が早い
	３．プログラムが短くて済む
"""

"""
	モジュールのインポート
	import Module
	import Module as Alias
	from Module import name

	他のサイトを見ると
	form Module import *
	とかいうインポート方法があるが、
	名前の由来がわかりにくく、バグが出やすいので使わない。
"""

import Tkinter as Tk

la = Tk.Label(None, text = "Hello, World!", font = ("Times", "18"))
la.pack()
la.mainloop()

"""
	import Tkinter as Tk
	Tkinter を Tk としてインポート
	
	la = Tk.Label(None, text = "Hello, World!", font = ("Times", "18"))
	Label を定義
	最初の引数は親ヴィジェットを指す。
	本文においては None なので親はいない。
	ヴィジェットとは GUI の部品という意味。
	text, font はキーワードパラメータ。
	Times 18pt を使って "Hello, World!" と書くラベルを作成して、la に代入している。
	...キーワードパラメータとは何ぞや
	...Times 18pt とは何ぞや
	...ラベルとは何ぞや
	
	la.pack()
	la を配置する。
	
	la.mainloop()
	mainloop メソッドを使って、la をアプリにする。（部品ではなく、プログラム全体にする）
	Tkinter のヴィジェットはこの mainloop メソッドによってアプリケーションになれる。
	通常は親無しのヴィジェットの mainloop を用いてアプリケーションを作れる。
"""

