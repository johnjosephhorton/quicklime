#! /usr/bin/perl

# Paolo Lulli 2012

use lib qw(lib);
use LimeSurvey;
use AptCaller;

my @dependencies = (    'mysql-client', 
			'mysql-server', 
			'apache2', 
			'php5', 
			'php5-mysql', 
			'php-cli');


&getLimeSurvey(); # Downloads the code from LimeSurvey website

#&aptInstall("<package-name>");

foreach my $dep (@dependencies){
	print "Installing package: [".$dep."]\n";
	&aptInstall($dep);
	print "DONE\n";
}

