#!/usr/bin/env python
import time

print "Content-Disposition: attachment; filename=demo/log.txt"
print "Set-Cookie: fileDownload=true"
print 'Content-Type: text/html\n'

import urllib2
response = urllib2.urlopen('http://localhost/demo/log.txt')
html = response.read()
print html
import time
time.sleep(5)

