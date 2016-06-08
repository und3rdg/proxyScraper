#!/bin/env python3

import socket
import threading
from queue import Queue
# import urllib.request


# IP ARRAY WITH IP RANGE
# ip = []
# def ipRange(aStart, aEnd, bStart, bEnd, cStart, cEnd, dStart, dEnd):
#     for a in range(aStart, aEnd + 1):
#         for b in range(bStart, bEnd + 1):
#             for c in range(cStart, cEnd + 1):
#                 for d in range(dStart, dEnd + 1):
#                     ipOut = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d) 
#                     ip.append(ipOut)

# ipRange(5,5,
#         135,150,
#         0,255,
#         0,255)

# print('list Ip Done')



# IP / PORT SCANNER

print_lock = threading.Lock()

openPort = []
# portRange = [3128, 1080, 10200, 8080]
portRange = [80, 22]

# IP range
aStart,bStart,cStart,dStart = 127,0,0,0
aEnd, bEnd, cEnd, dEnd      = 127,0,0,5 

def portscan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        with print_lock:
            s.settimeout(3)
            con = s.connect((ip, port))
            openPort.append( str(ip) + ':' + str(port) )
            print( '     ' + openPort[-1] + ' <-- is OPEN (*)---------(*)' )
            con.close()
    except:
        with print_lock:
            print( 'CLOSE ' + str(ip) + ':' + str(port) )
            pass

def threader():
    while True:
        worker = q.get()
        # for port in portRange:
        #     portscan(worker, port)
        portscan(worker[0], worker[1])
        q.task_done()

q = Queue()

# how many threads
thNum = 1000
for x in range(thNum):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# for worker in ip:
#     q.put(worker)

for a in range(aStart, aEnd + 1):
    for b in range(bStart, bEnd + 1):
        for c in range(cStart, cEnd + 1):
            for d in range(dStart, dEnd + 1):
                ipOut = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d) 
                # ip.append(ipOut)
                for portOut in portRange:
                    worker = [ipOut, portOut]
                    q.put(worker)
q.join()

print('===================== IP WITH OPEN PORTS START LIST =====================')
for oIp in openPort:
    print('                         ', oIp)
print('=====================  IP WITH OPEN PORTS END LIST  =====================')


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

