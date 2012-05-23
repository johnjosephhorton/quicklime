#! /usr/bin/python
#
# Paolo Lulli 2012

import os

dependencies = ["mysql-client", "mysql-server", "apache2", "php5", "php5-mysql", "php-cli"]

class Limesurvey:
	"""A class to manage LimeSurvey install"""

	def f(self,str):
       		print str

	def install_dependencies(self):
		for dep in dependencies:
			print dep
	def dbg(self,cmd):
		os.system(cmd)

	
if __name__ == "__main__":
	lm = Limesurvey()
	lm.install_dependencies()
	cmd = 'ls -l /usr/bin'
	lm.dbg(cmd)
