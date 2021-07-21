#try_except

"""
    例外が発生すると何も対応していなければそこでプログラムは停止する。
    何か対応して継続させたい場合は、例外が発生しうる部分を try 文のブロックに書き、発生時の対応処理を except のブロックに書く。
"""

while 1:
    usr = input("整数を入力：")
    try:
        integer = int(usr)
        print(integer)
        break #例外が発生しなければ while を抜ける
    except ValueError:
        print("小学校３年生からやり直せ雑魚。")

    """
        try の中で int(usr) ができなかったとき、例外が発生する。
        今回は ValueError とかいうエラーが起きる
        例外が起きると except の部分まで飛ぶ。
        
        import 正しいモジュール
        import 文法エラーをしているモジュール
        こいつはエラーを吐かない

        import 正しいモジュール
        try:
            import 文法エラーをしているモジュール
        except:
            print("文法エラーが発生しています。")

        こんな事もできる。
    """

