#!/bin/env python3

# import socket
# import urllib.request

def ipRange(aStart, aEnd, bStart, bEnd, cStart, cEnd, dStart, dEnd):
    for a in range(aStart, aEnd):
        for b in range(bStart, bEnd):
            for c in range(cStart, cEnd):
                for d in range(dStart, dEnd):
                    ipOut = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d) 
                    print('ping '+ipOut)
ipRange(168,169,192,193,0,255,0,255)

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

