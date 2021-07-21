apple_price = 200
money = 1000
input_count = input("購入する林檎の個数を入力して下さい。")
count = int(input_count)
total_price = apple_price * count
print("購入する林檎の個数は" + str(count) + "個です。")
print("支払い金額は" + str(total_price) + "円です。")
if money > total_price:
    print("林檎を" + str(count) = "個買いました。")
    print("残金は" + str(money - total_price) + "円です。")
elif money == total_price:
    print("林檎を" + str(count) + "個買いました。")
    print("財布が空になりました。")
else:
    print("お金が足りません。")
    print("林檎を変えませんでした。")
    
input("何かキーを押してください...")

"""
apple_price = 200
自動的に整数型が定義される。

input_count = "10"
自動的に文字列型が定義される。

str input(str 表示したい文字列)
input() の中に printf() scanf() が入ってる。
返り値は文字列型。

int int(引数)
引数を整数型に変換して返す

input_count = int(input("購入する～"))
ってすれば input_count を 整数型 に定義しつつ、この後の処理でそのまま input_count を無神経に使えて便利そう
ってか後々 str(count) ってするくらいなら str(count) を input_count にしてしまってもいいんじゃないか？

void print(str 表示したい文字列)
表示したい文字列を連結したいときは + を用いて連結できる。
printf("林檎を %s 個だけ購入しました。", input_count[]);
と
print("林檎を " + str(count) + " 個だけ購入しました。")
は同じ出力結果になる。

print(3 + 5) #8
print("3 + 5") #3 + 5

total = price * count
と、計算と格納はいつも通り
time +~ 1
もできる
time++
ができるのかはまだわからん。
% で余を計算できる

if 条件式 :
    真の処理
    #普通の if 文

elif 条件式 :
    真の処理
    # else if と同じ

else :
    偽の処理
    #普通の else

条件式をかっこでくくる必要はない、あってもなくてもいい

!= とか普通に使える

print() の引数に比較式を入れると True か False を表示してくれる
print(7 == 3 + 4) #True
みたいな
C でいうところの && は and とするみたい
同様に || は or みたい
尚、
10 < time and time < 18
は
10 < time < 18
と書けるらしい
否定
not z == 77
は
z != 77
と同じ
"""
