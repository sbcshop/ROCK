import ST7789
import time
import mraa as m
from PIL import Image,ImageDraw,ImageFont
import numpy as np
# Raspberry Pi pin configuration:
RST = 13
DC = 22
BL = 18

spi = m.Spi(0)

# 240x240 display with hardware SPI:
lcd = ST7789.ST7789(spi,RST, DC, BL)

# Initialize library.
lcd.Init()

# Clear display.
lcd.clear()

# Create blank image for drawing.
image1 = Image.new("RGB", (lcd.width, lcd.height), "WHITE")
draw = ImageDraw.Draw(image1)
font1 = ImageFont.truetype('fonts/FreeMonoBold.ttf', 16)
font2 = ImageFont.truetype('fonts/FreeMonoBold.ttf', 22)


draw.text((70, 70), 'Hello World ! ', font=font1, fill = "BLUE")
draw.text((40, 100), 'SB-Components ', font=font2, fill = "Red")

lcd.ShowImage(image1,0,0)
time.sleep(3)

image = Image.open('lcd_logo.jpg')	
lcd.ShowImage(image,0,0)

