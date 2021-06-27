from pyb import *
from time import sleep  

x=Pin('X1')        # 数据线连到了x1 口

def IR_receive():
    '''返回红外接收数据（10进制）'''
    global IR_ls
    IR_ls=[]
    n=0
    N=32
    while(x.value()):   # 等待信号出现
        sleep(0.0001)
    while(not x.value()):   # 跳过引导码
        sleep(0.0001)   
    while N:
        while(x.value()):   # 跳过结果码
        	sleep(0.0001)
    	while(not x.value()):
        	sleep(0.0001)
        while(x.value()):    # 高电平计时
            sleep(0.0001)
            n+=1
        if(n>=100):
            IR_ls.append('1')
        else:
            IR_ls.append('0')
        n=0
        N-=1                  
    if(IR_ls[0]=='0'):
	IR_data=IR_ls[16:24]
    else:
	IR_data=IR_ls[17:25]
    IR_data.reverse()         
    return int(''.join(IR_data),2)

while 1:
    sleep(0.5)
    data=IR_receive()   

    if(data==69):
        LED(1).toggle()
    elif(data==70):
        LED(2).toggle()

