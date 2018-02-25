#!/usr/bin/env python

# bounding poly module
def inBounds(pan, tilt):
    if pan > 90:
        return False
    if pan < -90:
        return False    
    if tilt > 90:
        return False
    if tilt < -90:
        return False
    return True

def inPanBounds(pan, tilt):
    if pan > 90:
        return False
    if pan < -90:
        return False
    return True

def inTiltBounds(tilt, pan):
    if tilt > 90:
        return False
    if tilt < -90:
        return False
    return True

def getMaxPan(tilt):
    return 90

def getMinPan(tilt):
    return -90

def getMaxTilt(pan):
    return 90

def getMinTilt(pan):
    return -90
