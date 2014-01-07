#!/usr/bin/env python
import time, Cookie

# Delay to make it realistic.
import time
time.sleep(5)

print "Content-Disposition: attachment; filename=pic.jpg"
print "Set-Cookie: fileDownload=true;path=/"
print 'Content-Type: text/html\n'


import urllib2
response = urllib2.urlopen('http://localhost/demo/pic.jpg')
html = response.read()
print html


