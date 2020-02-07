#!/bin/bash

sudo python3 /home/pi/raspi-myscreen/myscreen.py &> /home/pi/raspi-myscreen/log.txt &
firefox 'http://localhost/'
