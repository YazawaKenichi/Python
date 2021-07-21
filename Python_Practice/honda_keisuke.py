#本田圭佑とじゃんけんを再現する。

import random #random モジュールのインポート
import time #time モジュールのインポート

#「間」の定義 単位は秒
wl = 4 #YOU LOSE を表示する時間
maru = 2 #句読点の待ち時間
ten = 1 #句点の待ち時間
sour = 4 #ｼｭﾜｧ...の時間

#勝率の定義
win = 0.01 #単位は百分率
lose = 100 - win
you_lose_hand = ["パー", "グー", "チョキ"]
you_win_hand = ["チョキ", "パー", "グー"]
player_hand = ["グー", "チョキ", "パー"]

while True:
    #じゃんけん...
    print("じゃんけん...")
    time.sleep(ten)
    print("（ グー => 1 | チョキ => 2 | パー => 3 ）")
    try:
        player = int(input(">"))
        if(player != 1 and player != 2 and player != 3):
            print("")
            print("あなた数字読めます？")
            time.sleep(maru)
            print("一年間何やってたんですか。")
            print("")
        else:
            player -= 1
            print("")
            print("ぽん！")
            print("あ な た：" + player_hand[player])

            if(random.randrange(1, 101, 1) <= lose):
                #プレイヤーが負けの処理
                print("本田圭佑："+ you_lose_hand[player])
                time.sleep(wl/3)
                print("")
                time.sleep(wl/3)
                print("YOU LOSE")
                time.sleep(wl/3)
                print("")
                time.sleep(wl)
                print("俺の勝ち！")
                time.sleep(maru)
                if(player == 0):
                    print("負けは次に繋がる")
                    time.sleep(ten)
                    print("チャンスです。")
                    time.sleep(maru)
                    print("ネバーギブアップ！")
                elif(player == 1):
                    print("たかがじゃんけん、")
                    time.sleep(ten)
                    print("そう思ってないですか？")
                    time.sleep(maru)
                    print("それやったら明日も")
                    time.sleep(ten)
                    print("俺が勝ちますよ。")
                elif(player == 2):
                    print("何で負けたか、明日まで")
                    time.sleep(ten)
                    print("考えといてください。")
                    time.sleep(maru)
                    print("そしたら何かが")
                    time.sleep(ten)
                    print("見えてくるはずです。")
                time.sleep(maru)
                print("ほな、いただきます。")
                print("")
                time.sleep(sour)
                print("一日一回勝負。")
                time.sleep(maru)
                print("じゃあ、また明日。")
                time.sleep(maru)
                print("")
                retry = input("何かキーを押して再挑戦。c 入力で怖気づいて逃げる。>")
                print("")
                if (retry == "c"):
                    break
            else:
                #プレイヤーが勝ちの処理
                print("本田圭佑："+ you_win_hand[player])
                time.sleep(wl/3)
                print("")
                time.sleep(wl/3)
                print("YOU WIN")
                time.sleep(wl/3)
                print("")
                time.sleep(wl)
                print("やるやん！")
                time.sleep(maru)
                print("明日は俺にリベンジさせて。")
                time.sleep(maru)
                print("では、どうぞ")
                time.sleep(maru)
                print("")
                retry = input("何かキーを押してもう一回負かす。c 入力で勝ち逃げする。>")
                print("")
                if(retry == "c"):
                    break
    except:
        print("")
        print("あなた数字読めます？")
        time.sleep(maru)
        print("一年間何やってたんですか。")
        print("")

"""
random モジュールについて

random.randrange(start, stop, step)
start から (stop - 1) までの整数値からランダムに選ばれた値を返す。
step は選ぶ数値のステップ量（こう言ってもむずいな）
例）start = 1, stop = 10, step = 2 の時
1, 3, 5, 7, 9 のうちからランダムで選ばれる。
start = 10, stop = 100, step = 5 の時
10, 15, 20, 25, 30, 35, 40, 45,50, 55, 60, 65, 70, 75, 80, 85, 90, 95 のうちからランダムで選ばれる。
つまり選ばれる数が、初項 start 公差 step で stop 以下の数列の中からランダムで選択されるという事。
"""