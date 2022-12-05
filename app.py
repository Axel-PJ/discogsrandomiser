import discogs_client
import re
import random
import time

d = discogs_client.Client('DiscogsRandomiser/0.1', user_token=open(".token", "r").readline())
me=d.identity()
me.collection_folders[0].releases
collection = []
group=0

type(collection)

for item in me.collection_folders[0].releases:
    collection.append(item.release.title + " - " + re.sub(r"\(.\)", '' ,item.release.artists[0].name))

random.shuffle(collection)

while True:
    for idx, items in enumerate(collection[group:group+6]):
        print(items + " ["+ str(idx) + "]")
    print("---")
    time.sleep(15)
    group = group+6
    if group >= len(collection):
        group=0