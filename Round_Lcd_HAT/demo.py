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
from datetime import datetime


Font1 = ImageFont.truetype("Font/Font02.ttf",45)
Font2 = ImageFont.truetype("Font/Font02.ttf",20)

spi = mraa.Spi(0)

RST = 13
DC = 22
BL = 12

logging.basicConfig(level=logging.DEBUG)

disp = RoundLCD.RoundLCD_HAT(spi,RST, DC, BL)
disp.Init()
disp.clear()
 
image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
draw2 = ImageDraw.Draw(image2)
now = datetime.now() # current date and time
time1 = now.strftime("%H:%M:%S")
date1 = now.strftime("%d/%m/%Y")

draw2.arc((1,1,237,237),0, 360, fill =(26,246,136), width=9)
draw2.text((55, 90), time1, font=Font1, fill = (255,255,255))
draw2.text((75, 138), date1, font=Font2, fill = (255,255,255))
im_r2=image2.rotate(0)
disp.ShowImage(im_r2)
                
