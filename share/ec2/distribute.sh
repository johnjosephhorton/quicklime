#! /bin/bash -x

cd $(dirname $0)

scp -i $HOME/.keys/pl-odesk -r ../script/ ubuntu@ec2-46-51-165-177.eu-west-1.compute.amazonaws.com:
