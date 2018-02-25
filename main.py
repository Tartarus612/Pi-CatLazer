#!/usr/bin/env python

import math
import time
import random

import lazer

import figureEight
import circle
import razzleDazzle


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins
startTriggerPin = 19
dimLazerPin = 6
brightLazerPin = 0


GPIO.setup(startTriggerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
centerFloorPan = 0
centerFloorTilt = 60
centerWallPan = 0
centerWallTilt = 0
centerCeilingPan = 0
centerCeilingTilt = 0

centerFloorRadius = 40

def run(pin):

    timeToRun = random.randrange(360,600)
    endTime = time.time() + timeToRun

    print("running " + str(timeToRun) + " seconds")
    
    lazer.on(dimLazerPin, brightLazerPin)
    
    lastRunFunction = -1
    functionToRun = -1
    while time.time() < endTime:
        while(lastRunFunction == functionToRun):
            functionToRun = random.randrange(0,5)
        lastRunFunction = functionToRun
        functionRunTime = random.randrange(60,240)
        functionEndTime = time.time() + functionRunTime
        if(endTime < functionEndTime):
            functionEndTime = endTime
        print("functionToRun=" + str(functionToRun) + " for " + str(functionRunTime) +" seconds")
        if functionToRun == 0:
            figureEight.run(centerFloorPan, centerFloorTilt, centerFloorRadius * 1.5, functionEndTime)
        if functionToRun == 1:
            figureEight.run(centerFloorPan, centerFloorTilt, centerFloorRadius/2, functionEndTime)
        if functionToRun == 2:
            circle.run(centerFloorPan, centerFloorTilt, centerFloorRadius/1.5, functionEndTime)
        if functionToRun == 3:
            circle.run(centerFloorPan, centerFloorTilt, centerFloorRadius/3.5, functionEndTime)
        if functionToRun == 4:
            razzleDazzle.run(centerFloorPan, centerFloorTilt, centerFloorRadius, functionEndTime)
        if functionToRun == 5:
            razzleDazzle.run(centerFloorPan, centerFloorTilt, centerFloorRadius/4, functionEndTime)


    lazer.off()

GPIO.add_event_detect(startTriggerPin, GPIO.FALLING, run, 1000)



##while True:
##    # Get the time in seconds
##    t = time.time()
##
##    # G enerate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
##    a = math.sin(t * 2) * 90
##    
##    # Cast a to int for v0.0.2
##    a = int(a)
##    if(boundingPoly.inBounds(a, a)):
##        pantilthat.pan(a)
##        pantilthat.tilt(a)
##
##    # Two decimal places is quite enough!
##    print(round(a,2))
##
##    # Sleep for a bit so we're not hammering the HAT with updates
##    time.sleep(0.005)
