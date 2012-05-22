#!/usr/bin/perl

# Paolo Lulli 2012

use strict;
use warnings;


our $apt_package_file; 

sub aptInstall(){
	($package) = @_;
	print "$package\n";
}

1;
