#! /usr/bin/python
#
# Paolo Lulli 2012

import os
import urllib2
import tarfile
import shutil

dependencies = ["mysql-client", "mysql-server", "apache2", "php5", "php5-mysql", "php-cli"]

url="http://download.limesurvey.org/Latest_stable_release/limesurvey192plus-build120517.tar.gz"
file_name = 'limesurvey.tar.gz'
download_dir = '/var/www/'

db_instance='limes_db'
db_user='limes_db'
db_password='limes_db'

class Limesurvey:
	"""A class to manage LimeSurvey install"""

	def f(self,str):
       		print str

	def install_dependencies(self):
		"""APT modules install"""
		for dep in dependencies:
			print 'Installing dependency: [' + dep + ']'
			cmdstring = 'DEBIAN_FRONTEND=noninteractive; apt-get -q -y install ' + dep
			print 'DEBUG: ' + cmdstring
			os.system(cmdstring)

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
	
	def db_install(self):
		print 'Installing db: [' + db_instance + ']'
		cmdstring = 'mysqladmin -u root create ' + db_instance #+ ' --password=""'# + root_db_password
		print 'DEBUG: ' + cmdstring
		os.system(cmdstring)

	def db_create_user(self):
		print 'Installing db: [' + db_instance + ']'
		cmdstring = 'echo "use ' + db_instance + '; GRANT ALL PRIVILEGES ON *.* TO \'' + db_user + '\'@\'localhost\' IDENTIFIED BY \'' + db_password + '\' WITH GRANT OPTION; "| mysql -u root '+  db_instance 
		print 'DEBUG: ' + cmdstring
		os.system(cmdstring)

	def apache_config(self):
		shutil.copy2('./config/apache2.template', '/etc/apache2/sites-available/limesurvey')
		os.symlink('/etc/apache2/sites-available/limesurvey', '/etc/apache2/sites-enabled/limesurvey')
	
	def limesurvey_config(self):
		shutil.copy2('./config/config.php.template', '/var/www/limesurvey/config.php')

	def apache_restart(self):
		restart_cmd='/etc/init.d/apache2 restart'
		os.system(restart_cmd)

	def post_install(self):
		cmd = 'cat /var/www/limesurvey/admin/install/create-mysql.sql | mysql -u root '+  db_instance
		os.system(cmd)
		# ALT: curl 127.0.0.1:80/limesurvey/admin/install/index.php
		shutil.rmtree('/var/www/limesurvey/admin/install')
		
# TODO
#
# - import limesurvey db
# - move away admin/install directory
# - clean up the config options

#/var/www/limesurvey/admin/install/create-mysql.sql
# cat /var/www/limesurvey/admin/install/create-mysql.sql  | mysql -u root  db_instance 
# rm -fr /var/www/limesurvey/admin/install

	
if __name__ == "__main__":
	lm = Limesurvey()
	#lm.install_dependencies()
	#lm.download_limesurvey()
	#lm.unpack_limesurvey()
	lm.db_install()
	lm.db_create_user()
	lm.apache_config()
	lm.limesurvey_config()
	lm.apache_restart()
	lm.post_install()
