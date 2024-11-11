#!/usr/bin/env python3
#############################################################################
# Filename    : SevenSegmentDisplay.py
# Description : Control SevenSegmentDisplay with 74HC595
# Author      : www.freenove.com
# modification: 2019/12/27
########################################################################
import RPi.GPIO as GPIO
import time

dataPin   = 18      # DS Pin of 74HC595(Pin14)
latchPin  = 16      # ST_CP Pin of 74HC595(Pin12)
clockPin = 12       # CH_CP Pin of 74HC595(Pin11)
digitPin = (11,13,15,19)
# SevenSegmentDisplay display the character "0"- "F" successively
num = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e]
def setup():
    GPIO.setmode(GPIO.BOARD)   # use PHYSICAL GPIO Numbering
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    for i in digitPin:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i,1)
    GPIO.output(digitPin[0],0)
    GPIO.output(digitPin[3],0)
    
       

def loop():
    while True:
        pass

def destroy():  
    GPIO.cleanup()
    exit()

if __name__ == '__main__': # Program entrance
    print ('Program is starting...' )
    setup() 
    try:
        loop()  
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()  
