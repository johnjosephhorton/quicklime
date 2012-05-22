#! /usr/bin/perl

# Paolo Lulli 2012

# Raw wrapper for underlying apt-commands

use strict;
use warnings;

sub aptInstall(){
	my ($package) = @_;
	print "$package\n";
	my $var= `yes| apt-get install $package`;
}

1;
