import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000
spi.cshigh = False
spi.mode = 0b00

try:
    resp = spi.xfer2([0x00, 126])
    time.sleep(2)
    resp = spi.xfer2([0x00, 129])
    time.sleep(2)
    
    for i in range(0, 130, 1):
        print("Write " + str(i) + " - ")
        resp = spi.xfer2([0x00, i])
        print("Read: " + str(len(resp)) + " " + str(resp[0]) + " " + str(resp[1]))
        time.sleep(.1)
        
    time.sleep(.2)
    for i in range(130, 0, -1):
        print("Write " + str(i) + " - ")
        resp = spi.xfer2([0x00, i])
        print("Read: " + str(len(resp)) + " " + str(resp[0]) + " " + str(resp[1]))
        time.sleep(.1)
        
finally:
    spi.close()