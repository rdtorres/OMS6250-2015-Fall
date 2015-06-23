#!/bin/bash

if [ -z $1 ]; then
    echo "Usage: run-firewall.sh <firewall config file>"
    exit
fi

cp $1 ~/pyretic/pyretic/modules/firewall-policies.cfg
cp firewall.py ~/pyretic/pyretic/modules
pushd ~/pyretic
python pyretic.py -m p0 pyretic.modules.firewall
popd
