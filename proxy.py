#!/bin/env python3

import socket
import threading
from queue import Queue
import time
import urllib.request
import re
start_time = time.time()


# IP / PORT SCANNER

print_lock = threading.Lock()

openPort = []
portRange = [81, 84, 3128, 1080, 10200, 8080]
# portRange = [80, 22]

dyndns = []

# how many threads
thNum = 150

aStart,bStart,cStart,dStart = 183,91,33,75
aEnd, bEnd, cEnd, dEnd      = 183,255,255,255 

def dynDns(proxy_ip):
# CHECK PROXY 
# timeout in sec
    # timeout = 1
    # socket.setdefaulttimeout(timeout)

# proxy_ip = '183.91.33.75:84'
    proxy_support = urllib.request.ProxyHandler({"http": proxy_ip})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    proxy_time_start = time.time()

    response = urllib.request.urlopen('http://checkip.dyndns.org')
    html = response.read()

    proxy_time = time.time() - proxy_time_start

    dynIp = re.findall(r'<body>Current IP Address: (.*?)</body>',str(html))
    print(dynIp[0]+':'+port, ", --- %s seconds ---" % proxy_time ) 

    dyndns_list.append(dynIp)


def portscan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        with print_lock:
            s.settimeout(5)
            con = s.connect((ip, port))
            openPort.append( str(ip) + ':' + str(port) )
            print( '     ' + openPort[-1] + ' <-- is OPEN (*)---------(*)' )

            dyndns(openPort[-1])
            con.close()
    except:
        # with print_lock:
        #     print( 'CLOSED ' + str(ip) + ':' + str(port) )
        pass

def threader():
    while True:
        worker = q.get()
        # for port in portRange:
        #     portscan(worker, port)
        portscan(worker[0], worker[1])
        q.task_done()

q = Queue()

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


print( "Total time --- %s seconds ---" % (time.time() - start_time) )

