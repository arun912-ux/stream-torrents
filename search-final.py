import sys
import http.client
import re
from types import NoneType
import subprocess, sys
from time import sleep


#print(len(sys.argv))
s=""

lengthOfArgs = len(sys.argv)
# print(lengthOfArgs)

if(lengthOfArgs == 1):
    s = input("Enter name: ").replace(" ", "+")
else:
    for i in range(1, lengthOfArgs):
        #print(sys.argv[i])
        s = s + sys.argv[i] + "+"


# print(s)
query = s
# ct.function(s)

conn = http.client.HTTPSConnection("1337x.wtf")

headers = {
    'accept-charset': "utf-8",
    'cache-control': "no-cache"
    }


sear = "/search/" + query + "/1/"
conn.request("GET", sear , headers=headers)

res = conn.getresponse()
data = res.read()
resp = data.decode('utf-8')

fi = open('rep.txt', 'w', encoding = 'utf-8')
fi.write(resp)
fi.close()

fi = open('rep.txt', 'r', encoding = 'utf-8')

# m = re.search("torrent\/[0-9]{7}\/[a-zA-Z0-9?%-]*/", fi.readlines())

# for i in range(0, len(m.group())):
#     print(m.group(1))
i=1
lis=[]
for line in fi.readlines():
    # print(line)
    k = line.find('torrent/')
    if(k != -1):
        # print(line)cl
        # n = line.index("torrent\/[0-9]{7}\/[a-zA-Z0-9?%-]*/")
        # print()
        m = re.search("torrent\/[0-9]{7}\/[a-zA-Z0-9?%-]*/", line)
        if (type(m) != NoneType):
            print(str(i) + " " + m.group(0))
            i+=1
            lis.append(m.group(0))
        # break
    # print(k)

fi.close()

n = int(input("Enter number : "))
torrent = lis[n-1]

conn = http.client.HTTPSConnection("1337x.wtf")

headers = {
    'accept-charset': "utf-8",
    'cache-control': "no-cache"
    }


conn.request("GET", "/"+torrent, headers=headers)


res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))
resp = data.decode('utf-8')
m = re.search("magnet:\?xt=urn:btih:[a-zA-Z0-9&=%+\.-]*", resp)
# print(m.group(0))



magnet = m.group(0)

# print(magnet)

runcmd = "peerflix.cmd \"" + magnet + "\" --vlc"
print(runcmd)

# ps = open('file.ps1', 'w', encoding='utf-8')
# ps.write(runcmd)
# ps.close()

sleep(2)

p = subprocess.Popen(runcmd, stdout=sys.stdout)

p.communicate()
