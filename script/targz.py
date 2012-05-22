#! /usr/bin/python
#
# Paolo lulli 2012
#

import tarfile

tar = tarfile.open("limesurvey.tar.gz")
tar.extractall()
tar.close()
