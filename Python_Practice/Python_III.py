import utils
#utils ファイルが作成されていないので動かない。
#サイトを解析するかコードを読んで自作すれば動く。がんばれ。（他力本願）

import random

print("じゃんけんを始めます。")
player_name = input("お名前を入力してください。：")
print("何を出しますか？（0: グー, 1: チョキ, 2: パー）")
player_hand = int(input("数字で入力してください。："))

if utls.validate(player_hand):
    computer_hand = random.randint(0, 2)

    if player_name == "":
        utils.print_hand(player_hand)
    else:
        utls.print_hand(player_hand, player_name)
    
    utils.print_hand(computer_hand, "コンピュータ")

    result = utils.judge(player_hand, computer_hand)
    print("結果は " + result + " でした。")
else:
    print("正しい数値を入力してください")