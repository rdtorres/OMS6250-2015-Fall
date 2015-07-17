#!/bin/bash

#if [ -z $1 ]; then
#    echo "Usage: run-firewall.sh <firewall config file>"
#    exit
#fi

cp pyretic_switch.py ~/pyretic/pyretic/modules
pushd ~/pyretic
python pyretic.py -m p0 pyretic.modules.pyretic_switch
popd
