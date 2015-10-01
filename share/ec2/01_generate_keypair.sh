#! /bin/sh -x

cd $(dirname $0)

./lib/aws  --region=eu-west-1 add-keypair pl-odesk

