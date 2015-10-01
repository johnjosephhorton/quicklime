#! /bin/sh -x

cd $(dirname $0)

./lib/aws run-instances --region=eu-west-1 -k pl-odesk ami-e1e8d395 -t t1.micro
