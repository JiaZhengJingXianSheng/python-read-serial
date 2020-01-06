import serial
import serial.tools.list_ports
from time import sleep
import re
import matplotlib.pyplot as plt


def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data

if __name__ == '__main__':
    serial = serial.Serial('COM8', 9600, timeout=0.5)
    if serial.isOpen() :
        print("open success") 

        time_show=[]
        temp_show=[]
        over_temp=[]
        over_time=[]
 	
        plt.figure("By 物网三巨头")
        plt.ion()
        plt.grid(True)
        plt.xlabel('times')
        plt.ylabel('Tempature')
        plt.title('Tempature detection')
    else :
        print("open failed")


    t = 0
    while True:
        c=[]
        
        data =recv(serial)
        if data != b'' :
           
            b=re.compile(r'\d+').findall(str(data))
            if len(b) == 1:
                a = eval(b[0])
                
                if a>10:
                    t=t+1
                    if a>30:
                        over_temp.append(a)
                        over_time.append(t)
                        
                        print("！！！警告：温度过高！！！")
                        print('温度：'+str(a)+"C \n\n")
                        
                    else:
                        
                        print("**********")
                        print("温度正常")
                        print('温度：'+str(a)+"C \n\n")
                    temp_show.append(a)
                    time_show.append(t)
                    plt.plot(time_show,temp_show,'o-g')
                    plt.plot(over_time,over_temp,'or')
                    plt.draw()
        plt.pause(0.002)
                