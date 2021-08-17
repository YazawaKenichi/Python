#while

def difference():
    n = 0
    print("等差数列モード")
    a_1 = int(input("初項："))
    d = int(input("公差："))

    while 1 :
        n += 1
        a_n = a_1 + (n - 1) * d
        c = input("a_" + str(n) + " = " + str(a_n))
        if c == "c":
            break #while を出る
        if c != "c":
            continue #while を続ける

def ratio():
    n = 0
    print("等比数列モード")
    b_1 = int(input("初項："))
    r = int(input("公比："))

    while 1:
        n += 1
        b_n = b_1 * pow(r, n - 1)
        c = input("b_" + str(n) + " = " + str(b_n))
        if c == "c":
            break
        if c != "c":
            continue

def floor():
    n = 0
    print("階差数列モード")
    c_n = int(input("   初項："))
    d_1 = int(input("階差初項："))
    d   = int(input("   階差："))

    while 1:
        n += 1
        d_n = d_1 + (n - 1) * d
        c_n += d_n
        c = input("c_ " +  str(n) + " = " + str(c_n))
        if c == "c":
            break
        if c != "c":
            continue
while 1:
    mode = int(input("1.等差数列｜2.等比数列｜3.階差数列｜0.終了："))
    if mode == 1:
        difference()
    if mode == 2:
        ratio()
    if mode == 3:
        floor()
    if mode == 0:
        break
    if mode != 0 and mode == 1 and mode == 2 and mode == 3:
        continue

"""
while 条件式：
    処理
処理は条件式が真の時ループする

break
繰り返しの終了

continue
繰り返しの続行

特定の回数だけ繰り返す処理は、range 関数を用いた for 文が便利。
とかいう文章があったけど...
一体どういう意味やねん、普通の for 文と何が違うねん。
リスト・タプル・セット・辞書 といったコンテナの要素を順次処理していくなら、for 文を使う。（らしい）
リンクに飛びたい
"""
