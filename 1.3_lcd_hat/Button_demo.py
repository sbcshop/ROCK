# -*- coding:utf-8 -*-
import ST7789
import time
import mraa 
import mraa
from PIL import Image,ImageDraw,ImageFont
import numpy as np

spi = mraa.Spi(0)

# Raspberry Pi pin configuration:
RST = 13
DC = 22
BL = 18

KEY_UP_PIN     = 37 
KEY_DOWN_PIN   = 31
KEY_LEFT_PIN   = 33 
KEY_RIGHT_PIN  = 29
KEY_PRESS_PIN  = 35 

KEY1_PIN       = 40
KEY2_PIN       = 38
KEY3_PIN       = 36
KEY4_PIN       = 32


# 240x240 display with hardware SPI:
disp = ST7789.ST7789(spi,RST, DC, BL)
disp.Init()

# Clear display.
disp.clear()

KEY_UP_PIN = mraa.Gpio(KEY_UP_PIN)
KEY_DOWN_PIN = mraa.Gpio(KEY_DOWN_PIN)
KEY_LEFT_PIN = mraa.Gpio(KEY_LEFT_PIN)
KEY_RIGHT_PIN = mraa.Gpio(KEY_RIGHT_PIN)
KEY_PRESS_PIN = mraa.Gpio(KEY_PRESS_PIN)

KEY1_PIN = mraa.Gpio(KEY1_PIN)
KEY2_PIN = mraa.Gpio(KEY2_PIN)
KEY3_PIN = mraa.Gpio(KEY3_PIN)
KEY4_PIN = mraa.Gpio(KEY4_PIN)

KEY_UP_PIN.dir(mraa.DIR_IN)
KEY_DOWN_PIN.dir(mraa.DIR_IN)
KEY_LEFT_PIN.dir(mraa.DIR_IN)
KEY_RIGHT_PIN.dir(mraa.DIR_IN)
KEY_PRESS_PIN.dir(mraa.DIR_IN)

KEY1_PIN.dir(mraa.DIR_IN)
KEY2_PIN.dir(mraa.DIR_IN)
KEY3_PIN.dir(mraa.DIR_IN)
KEY4_PIN.dir(mraa.DIR_IN)

KEY_UP_PIN.mode(mraa.MODE_PULLUP)
KEY_DOWN_PIN.mode(mraa.MODE_PULLUP)
KEY_LEFT_PIN.mode(mraa.MODE_PULLUP)
KEY_RIGHT_PIN.mode(mraa.MODE_PULLUP)
KEY_PRESS_PIN.mode(mraa.MODE_PULLUP)

KEY1_PIN.mode(mraa.MODE_PULLUP)
KEY2_PIN.mode(mraa.MODE_PULLUP)
KEY3_PIN.mode(mraa.MODE_PULLUP)
KEY4_PIN.mode(mraa.MODE_PULLUP)


# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = 240
height = 240
image = Image.new('RGB', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
disp.ShowImage(image,0,0)

draw.text((80, 220), 'SB-Components ', fill = "WHITE")

# try:
while 1:
    # with canvas(device) as draw:
    if KEY_UP_PIN.read(): # button is released
        draw.polygon([(120, 50), (100, 100), (140, 100)], outline=255, fill="blue")  #Up
    else: # button is pressed:
        draw.polygon([(120, 50), (100, 100), (140, 100)], outline=255, fill=0)  #Up filled
        print ("Up")
        
    if KEY_LEFT_PIN.read(): # button is released
        draw.polygon([(50, 120), (100, 100), (100, 140)], outline=255, fill="blue")  #left           
    else: # button is pressed:
        draw.polygon([(50, 120), (100, 100), (100, 140)], outline=255, fill=0)  #left filled
        print ("left") 
        
    if KEY_RIGHT_PIN.read(): # button is released
        draw.polygon([(190, 120), (140, 100), (140, 140)], outline=255, fill="blue") #right        
    else: # button is pressed:
        draw.polygon([(190, 120), (140, 100), (140, 140)], outline=255, fill=0) #right filled
        print ("right")
        
    if KEY_DOWN_PIN.read(): # button is released
        draw.polygon([(120, 190), (140, 140), (100, 140)], outline=255, fill="blue") #down        
    else: # button is pressed:
        draw.polygon([(120, 190), (140, 140), (100, 140)], outline=255, fill=0) #down filled
        print ("down")
        
    if KEY_PRESS_PIN.read(): # button is released
        draw.rectangle((140, 140,100,100), outline=255, fill="red") #center         
    else: # button is pressed:
        draw.rectangle((140, 140,100,100), outline=255, fill=0) #center filled
        print ("center")
        
    if KEY1_PIN.read(): # button is released
        draw.ellipse((0,0,30,30), outline=255, fill="orange") #A button        
    else: # button is pressed:
        draw.ellipse((0,0,30,30), outline=255, fill=0) #A button filled
        print ("KEY1")
        
    if KEY2_PIN.read(): # button is released
        draw.ellipse((60,0,90,30), outline=255, fill="orange") #B button]        
    else: # button is pressed:
        draw.ellipse((60,0,90,30), outline=255, fill=0) #B button filled
        print ("KEY2")
        
    if KEY3_PIN.read(): # button is released
        draw.ellipse((120,0,150,30), outline=255, fill="orange") #A button        
    else: # button is pressed:
        draw.ellipse((120,0,150,30), outline=255, fill=0) #A button filled
        print ("KEY3")

    if KEY4_PIN.read(): # button is released
        draw.ellipse((180,0,210,30), outline=255, fill="orange") #A button        
    else: # button is pressed:
        draw.ellipse((180,0,210,30), outline=255, fill=0) #A button filled
        print ("KEY4")
    disp.ShowImage(image,0,0)

