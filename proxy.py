#!/bin/env python3

import socket
import threading
from queue import Queue
# import urllib.request


# IP ARRAY WITH IP RANGE
ip = []
def ipRange(aStart, aEnd, bStart, bEnd, cStart, cEnd, dStart, dEnd):
    for a in range(aStart, aEnd + 1):
        for b in range(bStart, bEnd + 1):
            for c in range(cStart, cEnd + 1):
                for d in range(dStart, dEnd + 1):
                    ipOut = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d) 
                    ip.append(ipOut)
ipRange(126,127,
        0,10,
        0,2,
        0,2)

# for i in ip:
#     print('ping', i)

# print('how many ip\'s: ', len(ip))
# print(ip[262144 - 1])
# print(ip[-1])




# IP / PORT SCANNER

print_lock = threading.Lock()

port = 22

def portscan(target):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print(target,':',port,'<-- IS OPEN ! ! !')
        con.close()
    except:
        # print(target, ':', port, 'dead')
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

# how many threads
thNum = 30
for x in range(thNum):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in ip:
    q.put(worker)

q.join()




# CHECK PROXY QUALITY
'''
# timeout in sec
timeout = 5
socket.setdefaulttimeout(timeout)

proxy_ip = '164.132.57.130:3128'
proxy_support = urllib.request.ProxyHandler({"http": proxy_ip})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

with urllib.request.urlopen('http://checkip.dyndns.org') as response:
    html = response.read()
print(html)
'''

