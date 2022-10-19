from audioop import mul
from encodings import utf_8
from ntpath import join
import re
with open("H:\/1.txt",'r',encoding="utf_8") as f:
    for i in f:
        for s in re.findall("http.*?'",i):
            mulu=s.split("\'")[0].split("/")[3:]
            mulu.pop(-1)
            # print(mulu)
            mulu="/".join(mulu)
            mkdir="mkdir -p /root/123/"+ mulu
            wget="cd /root/123/" + mulu + " && wget "+s.split("\'")[0]
            print(mkdir+"  &&   "+  wget)

        # print(re.findall("http.*?'",i)[-1])
        # print([1111,222][0])
        # print(str(re.findall("http.*?'",i)[0]).split("\'"))
