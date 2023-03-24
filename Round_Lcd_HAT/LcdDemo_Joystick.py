#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
from lib import RoundLCD
from PIL import Image,ImageDraw,ImageFont
import mraa
spi = mraa.Spi(0)

KEY_UP_PIN     = 37 
KEY_DOWN_PIN   = 31
KEY_LEFT_PIN   = 33 
KEY_RIGHT_PIN  = 29
KEY_PRESS_PIN  = 35 

KEY_UP_PIN = mraa.Gpio(KEY_UP_PIN)
KEY_DOWN_PIN = mraa.Gpio(KEY_DOWN_PIN)
KEY_LEFT_PIN = mraa.Gpio(KEY_LEFT_PIN)
KEY_RIGHT_PIN = mraa.Gpio(KEY_RIGHT_PIN)
KEY_PRESS_PIN = mraa.Gpio(KEY_PRESS_PIN)

KEY_UP_PIN.dir(mraa.DIR_IN)
KEY_DOWN_PIN.dir(mraa.DIR_IN)
KEY_LEFT_PIN.dir(mraa.DIR_IN)
KEY_RIGHT_PIN.dir(mraa.DIR_IN)
KEY_PRESS_PIN.dir(mraa.DIR_IN)

KEY_UP_PIN.mode(mraa.MODE_PULLUP)
KEY_DOWN_PIN.mode(mraa.MODE_PULLUP)
KEY_LEFT_PIN.mode(mraa.MODE_PULLUP)
KEY_RIGHT_PIN.mode(mraa.MODE_PULLUP)
KEY_PRESS_PIN.mode(mraa.MODE_PULLUP)

Font1 = ImageFont.truetype("Font/Font02.ttf",45)
Font2 = ImageFont.truetype("Font/Font02.ttf",20)


RST = 13
DC = 22
BL = 12

logging.basicConfig(level=logging.DEBUG)

try:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    disp = RoundLCD.RoundLCD_HAT(spi,RST, DC, BL)
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    

    image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")
    draw = ImageDraw.Draw(image1)
    #draw.arc((1,1,237,237),0, 360, fill =(0,0,255), width=9)
    im_r=image1.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(1)
    image = Image.open('pic/lcd_logo.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(2)

    image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
    draw2 = ImageDraw.Draw(image2)
    

    draw2.arc((1,1,240,240),0, 360, fill =(26,246,136), width=9)
       
    draw2.text((75, 90), "Hello !", font=Font1, fill = (255,255,255))
    draw2.text((90, 138), "Welcome", font=Font2, fill = (255,255,255))
    im_r2=image2.rotate(0)
    disp.ShowImage(im_r2)


    while True:
        if KEY_UP_PIN.read() == 0:
            
            draw2.arc((1,1,240,240),0, 360, fill =(0,153,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif KEY_LEFT_PIN.read()== 0:
            
            draw2.arc((1,1,240,240),0, 360, fill =(255,51,153), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif KEY_RIGHT_PIN.read()== 0:
            
            draw2.arc((1,1,240,240),0, 360, fill =(0,204,0), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif KEY_DOWN_PIN.read()== 0:
            
            draw2.arc((1,1,240,2407),0, 360, fill =(255,255,31), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif KEY_PRESS_PIN.read()== 0:
            
            draw2.arc((1,1,240,240),0, 360, fill =(255,255,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
