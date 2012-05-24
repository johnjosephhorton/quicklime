#! /bin/sh -x

./aws run-instances --region=eu-west-1 -k pl-odesk ami-e1e8d395 -t t1.micro
