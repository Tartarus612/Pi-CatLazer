import math
import time
from datetime import timedelta
import random

import pantilthat
import boundingPoly

def run(centerPan, centerTilt, radius, endTime):
    print("razzleDazzle running")
    #choose a random start
    pan = getPosition(radius, centerPan)
    tilt = getPosition(radius, centerPan)
    #set where the lazer is now
    currentPan = pan
    currentTilt = tilt
    #place the lazer on the razzle
    pantilthat.pan(pan)
    pantilthat.tilt(tilt)
    time.sleep(0.05)
    while time.time() < endTime:
        pan = getPosition(radius, centerPan)
        tilt = getPosition(radius, centerTilt)
        if(boundingPoly.inPanBounds(pan, tilt) == False):
            if(pan > boundingPoly.getMaxPan(tilt)):
                pan = boundingPoly.getMaxPan(tilt)
            if(pan < boundingPoly.getMinPan(tilt)):
                pan = boundingPoly.getMinPan(tilt)
        if(boundingPoly.inTiltBounds(tilt, pan) == False):
            if(tilt > boundingPoly.getMaxTilt(pan)):
                tilt = boundingPoly.getMaxTilt(pan)
            if(tilt < boundingPoly.getMinTilt(pan)):
                tilt = boundingPoly.getMinTilt(pan)      
                
        #print ("pan=" + str(pan) + " tilt=" + str(tilt))
        #print("current = " + str(time.time()) + " end = " + str(endTime))
        #need to slow down the servos between A and B, so do a mini update look thing.
        while (currentPan != pan and currentTilt != tilt):
            if(currentPan < pan):
                currentPan = currentPan + 1
            if (currentPan > pan):
                currentPan = currentPan - 1
            if (currentTilt < tilt):
                currentTilt = currentTilt + 1
            if (currentTilt > tilt):
                currentTilt = currentTilt -1
            pantilthat.pan(pan)
            pantilthat.tilt(tilt)
            time.sleep(.01)
        
        # Sleep for a bit so we're not hammering the HAT with updates
        time.sleep(0.5)

def getPosition(radius, center):
    return random.randrange(-(radius),radius) + center
