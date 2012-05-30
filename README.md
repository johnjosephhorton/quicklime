QuickLime
=========
Version 1.0 May 2012  
Developed by Paolo Lulli 

Copyright, oDesk Corporation 2012
GNU Public License 

    QuickLime is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    QuickLime is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    For details on the GNU Public License, see <http://www.gnu.org/licenses/>.

About QuickLime
------------------------------

LimeSurvey is a GPL licensed software to create surveys; it runs nicely on
a LAMP stack. <br/>
You can download it from [here] (http://download.limesurvey.org/Latest_stable_release/limesurvey192plus-build120517.tar.gz "limesurvey").
QuickLime is an installer for LimeSurvey. 

LimeSurvey, the easy way
------------------------------

QuickLime works in Ubuntu like a breeze.
You only have to launch the script as user <code>root</code>
<br/>
this way:<br/>
<code>cd script; ./quicklime </code>

it will:

- download latest LimeSurvey for you
- install all documented software dependencies
- create an Apache Virtual Server 
- create a database user for the application and load the required schema
- install LimeSurvey

 
Requirements
------------
QuickLime is written in Python, therefore you will need a working install of Python, together with the following modules:

- urllib2
- tarfile
- shutil

QuickLime is built on Ubuntu 12 64bit LTS; it is tested on an Ec2 
instance (Amazon Web Services). If you have access to AWS, you can simply 
start a new instance from the following AMI: <code> ami-e1e8d395 </code>

On the new instance, you will only need to transfer the code, i.e. doing:

<code>
scp -i <secret-key>.pem -r quicklime.tar.gz root@hostname:
</code>

or simply:

<code>
scp  -r quicklime.tar.gz root@&lt;hostname&gt;:
</code>

Then login on your brand new machine (or AMI instance):

<code>
ssh root@<hostname>:
tar vxzf quicklime.tar.gz
cd quicklime
</code>

Before launching the installer, there are some configurations that you can 
specify, like an SMTP to use to send email. Rather than having to do 
post-install configurations, you can change the configurations in 
the following file:

<code>config.py</code>

Above all, I would recommend editing the email and the SMTP server credentials:

<pre>
<code>
email_account='youremail@example.com'
email_password='custom_password'
siteadminbounce=''
sitename='QuickLime - LimeSurvey'
siteadminemail='admin@yourdomain.com'
emailmethod='smtp'
emailsmtphost='smtp.gmail.com'
emailsmtpuser='your-smtp_user@gmail.com'
emailsmtpssl='ssl'
emailsmtppassword='your-smtp-password'
</code>
</pre>

As long as the upstream LimeSurvey distribution may change over time, 
rather than having the repository URL hardcoded into the installer, you 
may need to change the download link  in the 
same configuration file:

<pre>
<code>
# Download URL of the limesurvey *.tar.gz 
download_url='http://www.limesurvey.org/en/stable-release/finish/25-latest-stable-release/457-limesurvey192plus-build120530zip'

#  file_name should contain the name of the *.tar.gz archive downloaded from the internet
file_name = 'limesurvey.tar.gz'
</code>
</pre>

Having a local copy of the LimeSurvey is also feasible, as long as the string <code>download_url</code>
uses a protocol supported by Python [urllib2] (http://docs.python.org/library/urllib2.html "urllib2")


Then, you are ready to launch the installer:

<pre><code>cd script
./quicklime
</code></pre>

QuickLime should basically work on any Debian-based distribution. It requires 
the following apt packages:

- mysql-client
- mysql-server
- apache2
- php5
- php5-mysql

plus the <code>curl</code> executable
