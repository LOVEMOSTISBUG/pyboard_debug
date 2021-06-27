# main.py -- put your code here!
from machine import I2C
from ssd1306 import SSD1306_I2C
import pyb
import micropython
micropython.alloc_emergency_exception_buf(100)
i2c=machine.I2C(-1, sda=machine.Pin("Y8"), scl=machine.Pin("Y6"), freq=400000)  
pyb.delay(1000)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

while 1:
        for i in range(1,41):
                filename="pic/"+str(i)+".bin"
                f = open(filename,"rb")
                num = f.read()
                oled.write_data(num)
                oled.show()
                pyb.delay(20)

