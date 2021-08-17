#menu_item がない
#food がない
#drink がない
#解析するか自作以下略

from food import Food #food.py の Food クラスを取得している？
from drink import Drink

food1 = Food("サンドイッチ", 500, 330) #Food クラスのインスタンスを生成
food2 = Food("チョコケーキ", 400., 450)
food3 = Food("シュークリーム", 200, 180)

foods = [food1, food2, food3] #foods 配列の作成

drink1 = Drink("コーヒー", 300, 100)
drink2 = Drink("オレンジジュース", 200, 350)
drink3 = Drink("エスプレッソ", 300, 30)

drinks = [drink1, drink2, drink3]

print("食べ物メニュー")
index = 0
for food in foods:
    print(str(index) + ". " + food.info()) #food.py の info() メソッドを利用
    index += 1

print("飲み物メニュー")
index = 0
for drink in drinks:
    print(str(index) + ". " + drink.info())
    index +=1

print("----------------------------------")
order = int(input("食べ物の番号を選択してください："))
selected_food = foods[order]

order = int(input("飲み物の番号を選択してください："))
selected_drink = foods[order]

count = int(input("何セット買いますか？（３個以上で１割引）："))
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
print("合計は " + str(result) + " 円です。")

#selected_food は foods[order] だが、そのあとの get_total_price(count) がわからん...
#おそらく foods[order] つまり Food(サンドイッチ～) のインスタンスの get_total_price() メソッドに count を渡しているのか？
#ぐぬ～、Food クラスの定義について勉強したい...