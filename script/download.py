import urllib2
response = urllib2.urlopen('http://www.google.com')
html = response.read()

