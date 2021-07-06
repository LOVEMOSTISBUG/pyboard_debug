import pyb
from pyb import Pin
from machine import I2C,Pin
from ssd1306 import SSD1306_I2C
from pyb import Switch
import ultrasonic


sw = Switch()
ult = ultrasonic.Ultrasonic('X1', 'X2')

i2c = I2C(sda=Pin("Y12"), scl=Pin("Y11"))   
 
oled = SSD1306_I2C(128, 32, i2c, addr=0x3c)
while 1:
    oled.text("Welcome!",0,0)             
    if sw.value() :
        oled.text(str(ult.distance_in_cm()),0,20)
    oled.show()  
    oled.fill(0)
