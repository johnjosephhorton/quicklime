#! /bin/bash -x

DB_INSTANCE="test_instance";
DB_USER="";
DB_PASS=""


echo "use $DB_INSTANCE ; GRANT ALL PRIVILEGES ON *.* TO '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASS' WITH GRANT OPTION; "| mysql -u root  $DB_INSTANCE -p



