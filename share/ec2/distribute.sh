#! /bin/bash -x

cd $(dirname $0)

scp -i $HOME/.keys/pl-odesk -r ../../script/ ubuntu@ec2-54-247-133-103.eu-west-1.compute.amazonaws.com:
