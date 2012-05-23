#! /usr/bin/python
#
# Paolo Lulli 2012

import os
import urllib2
import tarfile

dependencies = ["mysql-client", "mysql-server", "apache2", "php5", "php5-mysql", "php-cli"]

url="http://download.limesurvey.org/Latest_stable_release/limesurvey192plus-build120517.tar.gz"
file_name = 'limesurvey.tar.gz'
download_dir = '/opt/'
#download_dir = './'   ####### TODO comment out once tested


class Limesurvey:
	"""A class to manage LimeSurvey install"""

	def f(self,str):
       		print str

	def install_dependencies(self):
		"""APT modules install"""
		for dep in dependencies:
			print 'Installing dependency: [' + dep + ']'
			cmdstring = 'apt-get install ' + dep
			print 'DEBUG: ' + cmdstring
#			os.system(cmdstring)

	def download_limesurvey(self):
		u = urllib2.urlopen(url)
		#f = open(file_name, 'wb')
		f = open(download_dir + file_name, 'wb')
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

	def unpack_limesurvey(self):
		print 'Changing dir to: [' + download_dir + ']'
		os.chdir(download_dir)
		tar = tarfile.open(file_name)
		tar.extractall()
		tar.close()



	
if __name__ == "__main__":
	lm = Limesurvey()
	lm.install_dependencies()
	lm.download_limesurvey()
	lm.unpack_limesurvey()
