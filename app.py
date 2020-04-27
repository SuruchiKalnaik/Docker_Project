import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return """Hello World. You have visited {} times.\n<!DOCTYPE html>
<html>
<body style="background-color:deeppink;">

<h2 style="color:blue;font-size:300%;text-align:center;">7 Wonders Of World</h2>

<p style="color:chartreuse;font-size;300%;text-align:center;">Great Wall of China</p>
<p style="text-align:center;"><img src="https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/10/12/new-seven-wonders-great-wall-of-china.jpg.rend.hgtvcom.616.462.suffix/1491581549051.jpeg" alt="Great Wall of China" style="width:40%"></p>
<p style="text-align:center;"><a href="https://en.wikipedia.org/wiki/Great_Wall_of_China">About this</a></p>

<p style="color:chartreuse;font-size;300%;text-align:center;">Christ the Redeemer Statue</p>
<p style="text-align:center;"><img src="https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/10/12/new-seven-wonders-christ-the-redeemer.jpg.rend.hgtvcom.616.462.suffix/1491581548898.jpeg" alt="Christ the Redeemer Statue" style="width:40%"></p>
<p style="text-align:center;"><a href="https://en.wikipedia.org/wiki/Christ_the_Redeemer_(statue)">About this</a></p>

<p style="color:chartreuse;font-size;300%;text-align:center;">Machu Picchu</p>
<p style="text-align:center;"><img src="https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/10/12/new-seven-wonders-machu-picchu.jpg.rend.hgtvcom.616.462.suffix/1491581548990.jpeg" alt="Machu Picchu" style="width:40%"></p>
<p style="text-align:center;"><a href="https://en.wikipedia.org/wiki/Machu_Picchu">About this</a></p>

<p style="color:chartreuse;font-size;300%;text-align:center;">Chichen Itza</p>
<p style="text-align:center;"><img src="https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/10/12/new-seven-wonders-chichen-itza.jpg.rend.hgtvcom.616.462.suffix/1491581548887.jpeg" alt="Chichen Itza" style="width:40%"></p>
<p style="text-align:center;"><a href="https://en.wikipedia.org/wiki/Chichen_Itza">About this</a></p>

<p style="color:chartreuse;font-size;300%;text-align:center;">The Roman Colosseum</p>
<p style="text-align:center;"><img src="https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/10/12/new-seven-wonders-roman-coloesseum.jpg.rend.hgtvcom.616.462.suffix/1491581548881.jpeg" alt="The Roman Colosseum" style="width:40%"></p>
<p style="text-align:center;"><a href="https://en.wikipedia.org/wiki/Colosseum">About this</a></p>

<p style="color:chartreuse;font-size;300%;text-align:center;">Taj Mahal</p>
<p style="text-align:center;"><img src="https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/10/12/new-seven-wonders-taj-mahal.jpg.rend.hgtvcom.616.462.suffix/1491581548979.jpeg" alt="Taj Mahal" style="width:40%"></p>
<p style="text-align:center;"><a href="https://en.wikipedia.org/wiki/Taj_Mahal">About this</a></p>

<p style="color:chartreuse;font-size;300%;text-align:center;">Petra</p>
<p style="text-align:center;"><img src="https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/10/12/new-seven-wonders-petra.jpg.rend.hgtvcom.616.462.suffix/1491581549062.jpeg" alt="Petra" style="width:40%"></p>
<p style="text-align:center;"><a href="https://en.wikipedia.org/wiki/Petra">About this</a></p>

</body>
</html> """.format(count)
