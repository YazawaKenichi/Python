import twitter

_consumer_key = "DgxfUTIj7CktqOsSbSoDc4kZy"
_consumer_secret = "86yVwPR2I39bmq8kVVSVFGmEBeC9YnwoZsjXSsdcaE1eaU1Gvw"
_token = "AAAAAAAAAAAAAAAAAAAAAD1wXgEAAAAAHMvW5FTUqAdnzVmOuGgYynQnXm4%3DpNjYXiUB3cu105Byce2ZVrDDjNp3H40HkNie2yB1vF4D1HbxeN"
_token_secret = ""

auth = twitter.OAuth(consumer_key = _consumer_key, consumer_secret = _consumer_secret, token = _token, token_secret = _token_secret)

t = twitter.Twitter(auth = auth)

#
status = "Hello, World" #
t.statuses.update(status = status)

#
pic = ""
with open(pic, "rb") as image_file:
    image_data = image_file.read()
pic_upload = twitter.Twitter(domain = "upload.twitter.com", auth = auth)
id_img1 = pic_upload.media.upload(media = image_data)["media_id_string"]
t.statuses.update(status = status, media_ids = ",".join([id = img1]))

