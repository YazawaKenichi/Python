#

#ファイルを開く：open
reading_text = open("reading_text.txt", "r")
writing_text = open("writing_text.txt", "w")
additional_text = open("additional_text.txt", "a")
test_text = open("test_text.txt", "r")

#ファイルを閉める：close
test_text.close()

#ファイル全体の中身を見る
print(reading_text)

#ファイルを一行ずつ見る：for
for tmp in reading_text:
    print(tmp, end="") #end="" は改行を重ねないようにするもの

#ファイルの書き込み：write
writing_text.write("こんにちは。\n") #\nは改行

reading_text.close()
writing_text.close()
additional_text.close()
