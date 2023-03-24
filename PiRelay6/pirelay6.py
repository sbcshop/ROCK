#!/bin/python3

import mraa
import time

# Relay Pins
Relay_1 = 29
Relay_2 = 31
Relay_3 = 33
Relay_4 = 35
Relay_5 = 37
Relay_6 = 40

# initialise Relay GPIO as output
Relay1_GPIO = mraa.Gpio(Relay_1)
Relay2_GPIO = mraa.Gpio(Relay_2)
Relay3_GPIO = mraa.Gpio(Relay_3)
Relay4_GPIO = mraa.Gpio(Relay_4)
Relay5_GPIO = mraa.Gpio(Relay_5)
Relay6_GPIO = mraa.Gpio(Relay_6)

# set Relay GPIO to output
Relay1_GPIO.dir(mraa.DIR_OUT)
Relay2_GPIO.dir(mraa.DIR_OUT)
Relay3_GPIO.dir(mraa.DIR_OUT)
Relay4_GPIO.dir(mraa.DIR_OUT)
Relay5_GPIO.dir(mraa.DIR_OUT)
Relay6_GPIO.dir(mraa.DIR_OUT)

# toggle Relay pins 
try:
    while True:
    
        Relay1_GPIO.write(1)
        time.sleep(0.5)
        Relay2_GPIO.write(1)
        time.sleep(0.5)
        Relay3_GPIO.write(1)
        time.sleep(0.5)
        Relay4_GPIO.write(1)
        time.sleep(0.5)
        Relay5_GPIO.write(1)
        time.sleep(0.5)
        Relay6_GPIO.write(1)
        time.sleep(0.5)
        Relay1_GPIO.write(0)
        Relay2_GPIO.write(0)
        Relay3_GPIO.write(0)
        Relay4_GPIO.write(0)
        Relay5_GPIO.write(0)
        Relay6_GPIO.write(0)
        time.sleep(0.5)


except KeyboardInterrupt:
    print('Keyboard Interrupt')
    Relay1_GPIO.write(0)
    Relay2_GPIO.write(0)
    Relay3_GPIO.write(0)
    Relay4_GPIO.write(0)
    Relay5_GPIO.write(0)
    Relay6_GPIO.write(0)
