import math
import time
from datetime import timedelta
import random

import pantilthat
import boundingPoly

def run(centerPan, centerTilt, radius, endTime):
    print("circle running")
    #choose a random start
    currentAngle = random.randrange(0,360)
    #place the lazer on the circle
    pantilthat.pan(findX(currentAngle, radius, centerPan))
    pantilthat.tilt(findY(currentAngle, radius, centerTilt))
    time.sleep(0.05)
    while time.time() < endTime:
        if(currentAngle > 360):
            currentAngle = 0
        currentAngle += 1
        pan = findX(currentAngle, radius, centerPan)
        tilt = findY(currentAngle, radius, centerTilt)
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
                
        #print ("currentAngle="+ str(currentAngle) + " pan=" + str(pan) + " tilt=" + str(tilt))
        pantilthat.pan(pan)
        pantilthat.tilt(tilt)       
        
        
        
        # Sleep for a bit so we're not hammering the HAT with updates
        time.sleep(0.01)

def findX(position, radius, centerX):
    angle=(2 * math.pi / 360) * position
    return (centerX + radius * math.cos(angle))

def findY(position, radius, centerY):
    angle=(2 * math.pi / 360) * position
    return (centerY + radius * math.sin(angle))
