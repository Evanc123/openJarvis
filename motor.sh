#!/bin/bash          
echo Hello World
USERNAME=pi
HOSTS="10.0.1.7"
SCRIPT="cd ~/Desktop/; sudo python step.py"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
