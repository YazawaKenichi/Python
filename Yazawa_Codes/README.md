OpenCV 必須

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
