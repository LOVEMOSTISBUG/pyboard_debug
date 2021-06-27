from pyb import Servo
import pyb
import time
from pyb import Pin
 
p_out_1 = Pin('X17', Pin.OUT_PP)
p_out_2 = Pin('X18', Pin.OUT_PP)
p_out_1.low()
p_out_2.low()

xlights = (pyb.LED(2), pyb.LED(3))
ylights = (pyb.LED(1), pyb.LED(4))

s1 = Servo(1)
s1.angle(0)


accel = pyb.Accel()
SENSITIVITY = 8

while True:
    x = accel.x()
    if x > SENSITIVITY:
        xlights[0].on()       # 绿蓝等代表x方向
        xlights[1].off()
        s1.angle(-90)
    elif x < -SENSITIVITY:
        xlights[1].on()
        xlights[0].off()
        s1.angle(90)
    else:
        xlights[0].off()
        xlights[1].off()
        s1.angle(0)

    y = accel.y()
    if y > SENSITIVITY:
        ylights[0].on()
        ylights[1].off()
        p_out_1.high()
        # 红蓝灯代表y方向
    elif y < -SENSITIVITY:
        ylights[1].on()
        ylights[0].off()
        p_out_1.high()
    else:
        ylights[0].off()
        ylights[1].off()
        p_out_1.low()

    pyb.delay(100)
