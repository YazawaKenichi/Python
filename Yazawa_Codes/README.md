OpenCV 必須

<hr>

##### Windows 向けの解説。
[この主が作ったサイトの内容に加えて](https://kenichiyazawa.web.fc2.com/sources/How_to_Install_OpenCV.html)
[このサイトで紹介されているインストール](https://techacademy.jp/magazine/51404)も行う必要があるかも。

主が作ったサイトの手順を一通り行うと、```where opencv_version``` の段階で「見つかりません」的な表示がされる。
この where コマンドを打つ前の段階で環境変数に登録した C:\opencv\bin が存在していないからそのような表示がされてしまう。
opencv**.exe を実行すると、その exe のあるフォルダに opencv フォルダが展開される。
これを手動で C: 直下にコピーする必要がある。

ただどうやらこれだけでは「where で探すことができるが import はできない」という状態になる。
そこで、先ほど記述した TechAcademy のサイトを参考に opencv-python をインストールする必要がある。
環境変数の ```PATH``` に ```"C:\users\user\appdata\local\programs\python\python*\Scripts"``` を通す。
```
python -m pip install --upgrade pip
pip install opencv-python
pip install opencv-contrib-python
```
これでできるようになったはずだ。 

<hr>

##### Linux (Debian) 向け
まずそもそも Linux で Python を使ったことが無い場合は、最新版の Python をインストールする必要がある。
```
$ sudo apt autoremove python
```
を用いて、デフォルトで入っている Python を消す。
[こ↑こ↓](https://pythonlinks.python.jp/ja/index.html) から最新版 Python のソースファイルをダウンロードしてくる。
```
$ tar xJf Python-3.*.*.tar.xz
$ cd Python-3.*.*
$ ./configure
$ make
$ sudo make install
```
とすることで 最新版 Python がインストールされる。
最新版ではなくてもとにかく Python3 が入っていれば OpenCV は使用可能。
```
$ pip install opencv-python
```
とすることで OpenCV がインストールされる。

<hr>

##### Mac は知らん。自分でググれ
