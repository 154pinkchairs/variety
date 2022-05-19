import requests
import time
from time import sleep
def instance(instances):
    instances = ["https://libreddit.spike.codes", "https://libredd.it", "https://libreddit.dothq.co", "https://libreddit.kavin.rocks", "https://reddit.invak.id", "https://lr.riverside.rocks", "https://libreddit.strongthany.cc", "https://libreddit.privacy.com.de", "https://reddit.artemislena.eu", "https://libreddit.some-things.org", "https://reddit.stuehieyr.com", "https://lr.mint.lgbt", "https://libreddit.igna.rocks", "https://lr.oversold.host", "https://libreddit.de", "https://libreddit.pussthecat.org", "https://leddit.xyz", "https://libreddit.nl", "https://libreddit.bus-hit.me"]
    for i in instances:
        response = requests.get(i)
        time.sleep(2)
        isAlive= []
        isAlive = response.status_code() == str(200)
        #instances_alive = {i: f'is_alive={isAlive}'}
        break
    #instances_alive = {"https://libreddit.spike.codes": f"alive={isAlive}", "https://libredd.it": f"alive={isAlive}", "https://libreddit.dothq.co": f"alive={isAlive}", "https://libreddit.kavin.rocks": f"alive={isAlive}", "https://reddit.invak.id": f"alive={isAlive}", "https://lr.riverside.rocks": f"alive={isAlive}", "https://libreddit.strongthany.cc": f"alive={isAlive}", "https://libreddit.privacy.com.de": f"alive={isAlive}", "https://reddit.artemislena.eu": f"alive={isAlive}", "https://libreddit.some-things.org": f"alive={isAlive}", "https://reddit.stuehieyr.com": f"alive={isAlive}", "https://lr.mint.lgbt": f"alive={isAlive}", "https://libreddit.igna.rocks": f"alive={isAlive}", "https://lr.oversold.host": f"alive={isAlive}", "https://libreddit.de": f"alive={isAlive}", "https://libreddit.pussthecat.org": f"alive={isAlive}", "https://leddit.xyz": f"alive={isAlive}", "https://libreddit.nl": f"alive={isAlive}", "https://libreddit.bus-hit.me": f"alive={isAlive}"}
    print(isAlive)
    return
instance("https://libreddit.spike.codes")