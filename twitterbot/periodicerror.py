# なぜかうまく行かない。文法ミス
import twitter

CK = "Jfq0gkGTlwDh2IGG53S6uR04b"
CS = "mmRv1loUfwOlggWdA9zoQS0XjRoGEKmDTCeFamOeiZxH9zEKxX"
AT = "1295214616411168768-FFdgvtQ9FPlLFALgH6nM5zJZMxRXMs"
AS = "9Rmwg39nooQkjCiXXwWf5aXSM9gtk4bHOvS862wqL78rM"

auth = twitter.OAuth(consumer_key = CK, consumer_secret = CS, token = AT, token_secret = AS)

t = twitter.Twitter(auth = auth)

#
status = "Hello, World" #
t.statuses.update(status = status)

#
pic = "../nn-hokuson/1.png"
with open(pic, "rb") as image_file:
    image_data = image_file.read()
pic_upload = twitter.Twitter(domain = 'upload.twitter.com', auth = auth)
id_img1 = pic_upload.media.upload(media = image_data)["media_id_string"]
t.statuses.update(status = status, media_ids = ",".join([img1]))   # id = img1 に文法ミスがあるらしい

