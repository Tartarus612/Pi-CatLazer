#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import strftime, time, localtime

dimLazerPin = 0
brightLazerPin = 0

def on(dimPin, brightPin):
    global dimLazerPin
    dimLazerPin = dimPin
    global brightLazerPin
    brightLazerPin= brightPin
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    GPIO.setup(dimLazerPin,GPIO.OUT)
    GPIO.setup(brightLazerPin,GPIO.OUT)    
    print("LED on")
    if(int(strftime("%H", localtime())) <= 8 or int(strftime("%H", localtime())) >= 18):
        print("dim lazer")
        GPIO.output(dimLazerPin,GPIO.HIGH)
    else:
        print("bright lazer")
        GPIO.output(brightLazerPin,GPIO.HIGH)
        
        

def off():
    print("LED off")
    GPIO.output(dimLazerPin,GPIO.LOW)
    GPIO.output(brightLazerPin,GPIO.LOW)
