#!/bin/env python
import urllib
candidate_proxies = ['http://164.132.57.130:3128']
for proxy in candidate_proxies:
    print("Trying HTTP proxy %s" % proxy)
    try:
        result = urllib.urlopen("http://www.google.com", proxies={'http': proxy})
        print( "Got URL using proxy %s" % proxy)
        break
    except:
        print("Trying next proxy in 5 seconds")
        time.sleep(5)
