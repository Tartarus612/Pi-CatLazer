#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import strftime, time, localtime
import spidev

def on():
    print("LED on")
    if(int(strftime("%H", localtime())) <= 8 or int(strftime("%H", localtime())) >= 18):
        print("dim lazer")
        spi.xfer2([0x00, 126])
    else:
        print("bright lazer")
        spi.xfer2([0x00, 129])       
        

def off():
    print("LED off")
    spi.xfer2([0x00, 0])
