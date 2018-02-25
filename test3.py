#!/usr/bin/env python

# mcp4131.py
# 2016-01-06
# Public Domain

import time
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html

INCPOT=0x04
DECPOT=0x08

# 00h Volatile Wiper 0 
#   Write Data 0000 00nn nnnn nnnn
#   Read Data  0000 11nn nnnn nnnn
#   Increment  0000 0100
#   Decrement  0000 1000

# 01h Volatile Wiper 1
#   Write Data 0001 00nn nnnn nnnn
#   Read Data  0001 11nn nnnn nnnn
#   Increment  0001 0100
#   Decrement  0001 1000

# 02h-03h Reserved

# 04h TCON
#   Write Data 0100 00nn nnnn nnnn
#   Read Data  0100 11nn nnnn nnnn

# 05h Status
#   Read Data  0101 11nn nnnn nnnn

# 06h-0Fh Reserved

# SPI open flags

W3=(1<<9) # select 3-wire operation
W3N1=(1<<10) # switch to miso after one byte
U0=(1<<5) # don't set CE0
U1=(1<<6) # don't set CE1

pi = pigpio.pi() # Connect to local Pi.

digpot_write = pi.spi_open(1, 2000000, U0|U1) # first SPI open
digpot_read  = pi.spi_open(1,  50000, W3|W3N1|U0|U1) # 3-wire write 1 then read
adc          = pi.spi_open(0, 2000000, U0|U1)

inc = True

potpos = 0

try:

   while True:

      pi.spi_write(digpot_write, [0, potpos])

      (b, d) = pi.spi_xfer(digpot_read, [0x0C, 0])
      if b == 2:
         rpos = d[1]
      else:
         rpos = -1

      (b, d) = pi.spi_xfer(adc, [1, 0x80, 0])
      if b == 3:
         c1 = d[1] & 0x0F
         c2 = d[2]
         ch0 = (c1<<8)+c2
      else:
         ch0 = -1

      (b, d) = pi.spi_xfer(adc, [1, 0xC0, 0])
      if b == 3:
         c1 = d[1] & 0x0F
         c2 = d[2]
         ch1 = (c1<<8)+c2
      else:
         ch1 = -1

      print("0={:4d} 1={:4d} pot={} ({})".format(ch0, ch1, potpos, rpos))

      if inc:
         potpos += 1
         if potpos > 129:
            inc = False
            potpos = 129
      else:
         potpos -= 1
         if potpos < 0:
            inc = True
            potpos = 0

      """
      if inc:
         cmd = DECPOT
      else:
         cmd = INCPOT

      (b, d) = pi.spi_xfer(digpot, [cmd])
      if b == 1:
         dp = d[0]
      else:
         dp = -1

      if ch1 > 4090:
         inc = False
      elif ch1 < 10:
         inc = True
      """

      time.sleep(0.05)

except:
   pi.spi_close(digpot_read)
   pi.spi_close(digpot_write)
   pi.spi_close(adc)
   pi.stop()
   print("closed handle and stopped ")