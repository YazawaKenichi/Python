#import json
from requests_oauthlib import OAuth1Session

CK = "Jfq0gkGTlwDh2IGG53S6uR04b"
CS = "mmRv1loUfwOlggWdA9zoQS0XjRoGEKmDTCeFamOeiZxH9zEKxX"
AT = "1295214616411168768-FFdgvtQ9FPlLFALgH6nM5zJZMxRXMs"
AS = "9Rmwg39nooQkjCiXXwWf5aXSM9gtk4bHOvS862wqL78rM"

url = "https://api.twitter.com/1.1/statuses/update.json"

params = {"status" : "Hello, World!"}
twitter = OAuth1Session(CK, CS, AT, AS)
res = twitter.post(url, params = params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        print(line['user']['name'] + '::' + line['text'])
        print(line['created_at'])
        print('***********************')
else:
    print("Failed: %d" % res.status_code)


