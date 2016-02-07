#!/bin/bash          

USERNAME=pi
PASSWORD=robot1234
HOSTS="10.0.1.7"
SCRIPT="cd ~/Desktop/; sudo python open.py"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
