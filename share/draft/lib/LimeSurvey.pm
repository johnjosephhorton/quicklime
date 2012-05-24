#!/usr/bin/perl

# Paolo Lulli 2012

use strict;
use warnings;

use LWP::Simple;
use Archive::Tar;

our $limesurvey_url = 'http://download.limesurvey.org/Latest_stable_release/limesurvey192plus-build120517.tar.gz';
our $limesurvey_file = 'limesurvey.tar.gz';

sub getLimeSurvey(){
	getstore($limesurvey_url, $limesurvey_file);
	my $tar = Archive::Tar->new;
	$tar->read($limesurvey_file);
	$tar->extract();
}

1;
