#ジオコーディングする GUI アプリサンプルコード
#参考：https://www.gis-py.com/entry/py-tkinker
#
#このソフトを実行する前に geocoder をインストールする必要がある
# cmd > python -m pip install geocoder
# cmd > python -m pip install googlemaps

from tkinter import*
import geocoder

root = Tk()
root.geometry("300x150")
root.title("ジオコーディングツール")

#フレーム
frame = Frame(root, width = 300, height = 150, relief = SUNKEN)
frame.grid()

#ラベル作成
label_location = Label(frame, text = "場所", font = ("Meiryo", 12, "bold"), padx = 5, pady = 5)
label_location.grid(row = 0, column = 0, sticky = E)

label_lat = Label(frame, text= "緯度", font = ("Meiryo", 12, "bold"), padx = 5, pady = 5)
label_lat.grid(row = 1, column = 0, sticky = E)

label_lon = Label(frame, text = "経度", font = ("Meiryo", 12, "bold"), padx = 5, pady = 5) 
label_lon.grid(row = 2, column = 0, sticky = E)

#テキストボックス作成
textbox_location = StringVar()
textbox_location_entry = Entry(frame, textvariable = textbox_location, width = 30)
textbox_location_entry.grid(row = 1, column = 1)


textbox_lat = StringVar()
textbox_lat_entry = Entry(frame, textvariable = textbox_lat, width = 30)
textbox_lat_entry.configure(state = "readonly")
textbox_lat_entry.grid(row = 1, column = 1)

textbox_lon = StringVar()
textbox_lon_entry = Entry(frame, textvariable = textbox_lon, width = 30)
textbox_lon_entry.configure(state = "readonly")
textbox_lon_entry.grid(row = 2, column = 1)

#ジオコーディングを実行するメソッド
def exexute_geocoding():
    #一度テキストボックスを編集可能にする
    textbox_lat_entry.configure(state = "normal")
    textbox_lon_entry.configure(state = "normal")

    #ジオコーディング実行
    location = geocoder.osm(textbox_location.get())
    textbox_lat_entry.insert(END, locationlatlng[0])
    textbox_lat_entry.insert(END, locationlatlng[1])

    #テキストボックスを編集不可にする
    textbox_lat_entry.configure(state = "readonly")
    textbox_lon_entry.configure(state = "readonly")

def exexute_clear():
    #一度テキストボックスを編集可能にする
    textbox_lat_entry.configure(state = "normal")
    textbox_lon_entry.configure(state = "normal")

    textbox_lat_entry.delete(0, END)
    textbox_lon_entry.delete(0, END)
    textbox_location_entry.delete(0, END)

    #テキストボックスを編集不可にする
    textbox_lat_entry.configure(state = "readonly")
    textbox_lon_entry.configure(state = "readonly")

#ボタン作成
btn_execute = Button(frame, text = "実行", command = exexute_geocoding)
btn_execute.grid(row = 3, column = 1, sticky = E)
btn_clear = Button(frame, text = "クリア", command = exexute_clear)
btn_clear.grid(row = 3, column = 2, sticky = W)
root.mainloop()


