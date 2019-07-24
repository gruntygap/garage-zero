# Import required Python libraries
# import RPi.GPIO as GPIO
import time

pinList = [2]

def initialize():
    # Use BCM GPIO references instead of physical pin numbers
    #GPIO.setmode(GPIO.BCM)

    # init list with pin numbers
    # loop through pins and set mode and state to 'low'
    for i in pinList:
        print(i)
        #GPIO.setup(i, GPIO.OUT)
        #GPIO.output(i, GPIO.HIGH)

def trigger() :
        for i in pinList:
          #GPIO.output(i, GPIO.LOW)
          time.sleep(0.25)
          #GPIO.output(i, GPIO.HIGH)
          time.sleep(0.25)
          #GPIO.cleanup()

