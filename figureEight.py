import math
import time
from datetime import timedelta
import random

import pantilthat
import boundingPoly

def run(centerPan, centerTilt, radius, endTime):
    print("figureEight running")
    currentAngle = -1
    #place the lazer on the figure 8
    pantilthat.pan(findX(currentAngle, radius, centerPan))
    pantilthat.tilt(findY(currentAngle, radius, centerTilt))
    time.sleep(0.05)
    while time.time() < endTime:
        if(currentAngle > 64):#reset the angle to 8 to complete the loop
            currentAngle = 0
        currentAngle += 1
        pan = findX(currentAngle/10, radius, centerPan)
        tilt = findY(currentAngle/10, radius, centerTilt)
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
        time.sleep(0.02)

def findX(position, radius, centerX):
    top=radius*math.cos(position)
    bottom=1+math.pow(math.sin(position), 2)
    return (centerX + top/bottom)

def findY(position, radius, centerY):
    top=radius*math.sin(position)*math.cos(position)
    bottom=1+math.pow(math.sin(position), 2)
    return (centerY + top/bottom)
