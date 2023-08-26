import time
import dht
import glcdfont
from ili934xnew import ILI9341, color565
import tt14
import tt24
import tt32
from machine import Pin, SPI
from micropython import const
import math
from time import sleep
from random import randint
import os

SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(3)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)


TFT_CLK_PIN = const(6)
TFT_MOSI_PIN = const(7)
TFT_MISO_PIN = const(4)
TFT_CS_PIN = const(13)
TFT_RST_PIN = const(14)
TFT_DC_PIN = const(15)                
fonts = [glcdfont,tt14,tt24,tt32]
spi =   SPI(0,baudrate=31250000,
        miso=Pin(TFT_MISO_PIN),
        mosi=Pin(TFT_MOSI_PIN),
        sck=Pin(TFT_CLK_PIN))
print(spi)
print(os.uname())
display = ILI9341(
    spi,
    cs=Pin(TFT_CS_PIN),
    dc=Pin(TFT_DC_PIN),
    rst=Pin(TFT_RST_PIN),
    w=SCR_WIDTH,
    h=SCR_HEIGHT,
    r=SCR_ROT)

def circle(cx,cy,r,c):   # Centre (x,y), radius, color
    for angle in range(0, 360, 1):  # 0 to 360 degrees in 1 deg steps
        y=int(r*math.sin(math.radians(angle)))
        x=int(r*math.cos(math.radians(angle)))
        display.pixel(cx-x,cy+y,color=c)
while True:        
    display.set_pos(95,10)
    display.set_font(tt32)
    display.set_color(color565(0, 0, 0), color565(135, 135, 135))
    display.print("My Circle")#
    circle(155,125,50,1)
    circle(155,125,49,1)
