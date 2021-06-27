import pyb
import time
from pyb import Pin
 
p_out_1 = Pin('X17', Pin.OUT_PP)
p_out_2 = Pin('X18', Pin.OUT_PP)
p_out_3 = Pin('X19', Pin.OUT_PP)
p_out_4 = Pin('X20', Pin.OUT_PP)
p_out_1.low()
p_out_2.low()
p_out_3.low()
p_out_4.low()

intensity = 0


xlights = (pyb.LED(2), pyb.LED(3))
ylights = (pyb.LED(1), pyb.LED(4))


accel = pyb.Accel()
SENSITIVITY = 8

while True:
    x = accel.x()  # 绿黄等代表x方向
    if x > SENSITIVITY:
        xlights[0].on()      
        xlights[1].off()
        p_out_3.high()
        p_out_4.low()
        
    elif x < -SENSITIVITY:
        xlights[1].on()
        xlights[0].off()
        p_out_4.high()
        p_out_3.low()
        
    else:
        xlights[0].off()
        xlights[1].off()
        p_out_3.low()
        p_out_4.low()

    y = accel.y() # 红蓝灯代表y方向
    if y > SENSITIVITY:
        ylights[0].on()
        ylights[1].off()
        p_out_1.high()
        p_out_2.low()
    elif y < -SENSITIVITY:
        intensity =  int((SENSITIVITY/20)*150)
        ylights[1].intensity(intensity)
        ylights[0].off()
        p_out_2.high()
        p_out_1.low()
    else:
        ylights[0].off()
        ylights[1].off()
        p_out_1.low()
        p_out_2.low()

    pyb.delay(100)
