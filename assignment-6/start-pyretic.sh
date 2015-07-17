#!/bin/bash

#if [ -z $1 ]; then
#    echo "Usage: run-firewall.sh <firewall config file>"
#    exit
#fi

cp dns_amplification_prevention.py ~/pyretic/pyretic/modules
cp pyretic_switch.py ~/pyretic/pyretic/modules
cp firewall.py ~/pyretic/pyretic/modules
cp dns_firewall.py ~/pyretic/pyretic/modules
pushd ~/pyretic
python pyretic.py -m p0 pyretic.modules.dns_amplification_prevention
popd
