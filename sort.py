import json

src = "/home/ljd/workstation/tmp/SSRSpeed/results/subscribe-hk.json"
desc = "subscribe-hk.txt"

f = open(desc, 'w')
j = open(src, 'r')
origin = json.loads(j.read())

for o in origin:
    if o['dspeed'] / 1024 / 1024 > 50:
        print(o['link'])
        f.write(o['link']+"\n")

f.close()
j.close()
