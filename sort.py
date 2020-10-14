import json

src = "D:/CodeHub/github/SSRSpeed/results/2020-10-14-11-16-15.json"
desc = "quality.txt"

f = open(desc, 'w')
j = open(src, 'r')
origin = json.loads(j.read())

for o in origin:
    if o['dspeed'] / 1024 / 1024 > 40:
        print(o['link'])
        f.write(o['link']+"\n")

f.close()
j.close()