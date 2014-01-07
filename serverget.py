#!/usr/bin/env python

# Note the header here that will tell the browser to start a download. 

print "Content-Disposition: attachment; filename=log.txt"
print "Set-Cookie: fileDownload=true path=/;"
print 'Content-Type: text/html\n'

import urllib2
response = urllib2.urlopen('http://localhost/log.txt')
html = response.read()
print html
import time
time.sleep(5)  # pretent it takes longer to download.


