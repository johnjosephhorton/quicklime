QuickLime
=========

About QuickLime
------------------------------

LimeSurvey is a GPL licensed software to create surveys; it runs nicely on
a LAMP stack. <br/>
You can download it from [here] (http://download.limesurvey.org/Latest_stable_release/limesurvey192plus-build120517.tar.gz "limesurvey").
QuickLime is an installer for LimeSurvey. 

LimeSurvey, the easy way
------------------------------

QuickLime works in Ubuntu like a breeze.
You only have to launch the script as user <code>root</code>:
<pre><code>cd script
./quicklime
</code></pre>

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
scp -i <secret-key>.pem -r quicklime.tar.gz root@&lt;hostname&gt;:
</code>

or simply:

<code>
scp  -r quicklime.tar.gz root@&lthostname&gt;:
</code>

Then login on your brand new machine (or AMI instance):

<code>
ssh root@<hostname>:
tar vxzf quicklime.tar.gz
cd quicklime
</code>

and then, launch the installer:

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

#! /bin/bash -x

cd $(dirname $0)

