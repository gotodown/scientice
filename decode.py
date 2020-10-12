import os
import base64

path = "D:/CodeHub/github/scientice/freev2"

filelist = os.listdir(path)

f = open("final.txt", "a+")

for fl in filelist:
    if fl.endswith("txt"):
        print(fl,"------------")
        tmp = open(path+"/"+fl, "r")
        content = tmp.read()
        if "://" in content:
            f.write(content)
        else:
            url = base64.b64decode(tmp.read())
            # print(url)
            f.write(url.decode("utf-8"))
        tmp.close()
        # break



f.close()