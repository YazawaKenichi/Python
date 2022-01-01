#import json
from requests_oauthlib import OAuth1Session

CK = "Jfq0gkGTlwDh2IGG53S6uR04b"
CS = "mmRv1loUfwOlggWdA9zoQS0XjRoGEKmDTCeFamOeiZxH9zEKxX"
AT = "1295214616411168768-FFdgvtQ9FPlLFALgH6nM5zJZMxRXMs"
AS = "9Rmwg39nooQkjCiXXwWf5aXSM9gtk4bHOvS862wqL78rM"

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

params = {}
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params = params)

if req.status_code == 200:
    timelines = json.loads(req.text)
    for tweet in timelines:
        print(tweet["text"])
else:
    print("Failed: %d" % req.status_code)


