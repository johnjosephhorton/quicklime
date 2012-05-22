#! /usr/bin/python
# Paolo Lulli 2012
#
# Downloads LimeSurvey code base

import urllib2


url="http://download.limesurvey.org/Latest_stable_release/limesurvey192plus-build120517.tar.gz"
file_name = 'limesurvey.tar.gz'
download_dir = '/opt/'
download_dir = '.'
#file_name = url.split('/')[-1]


u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

