#!/bin/env python2
import urllib2, socket

inputfile = 'list/in.txt'
oututfile = 'list/out.txt'

timeout = 3
testurl = 'http://checkip.dyndns.org'
# colors 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

socket.setdefaulttimeout(timeout)
# read the list of proxy IPs in proxyList
# proxyList = ['172.30.1.1:8080', '172.30.3.3:8080'] # there are two sample proxy ip
proxyList = [] # there are two sample proxy ip
with open(inputfile) as proxy_file:
    proxyList = proxy_file.readlines()

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib2.ProxyHandler({'http': pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)        
        req=urllib2.Request(testurl)  # change the url address here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:

        print "ERROR:", detail
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print bcolors.FAIL + "Bad Proxy", item + bcolors.ENDC
    else:
        print bcolors.OKBLUE + item, "is working"+ bcolors.ENDC 
        with open(oututfile, "a") as out_file:
            out_file.write(item)

