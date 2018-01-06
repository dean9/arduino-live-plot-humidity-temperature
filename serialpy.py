import serial
import numpy as np
import matplotlib.pyplot as plt
import re
from drawnow import *
import datetime


serData = serial.Serial('/dev/ttyACM0', 9600)

humid = []
temp = []
plt.ion()
cnt = 0 


plt.subplots(nrows=2, ncols=1, sharex=True)
def plot():

    plt.subplot(2,1,1)
    #plt.gca().set_ylim(20,80)
    plt.plot(humid, c='blue')
    #plt.ylabel('Humidity')
    plt.grid(True)
    plt.legend('Humid.')

    plt.subplot(2,1,2)
    #plt.gca().set_ylim(0,50)
    plt.plot(temp, c='red')
    #plt.ylabel('Temperature')
    plt.grid(True)
    plt.legend('Temp.')



while True:
    if serData.inWaiting()>0:
        ardString = str(serData.readline())
        dataArray = re.findall(r"[-+]?\d*\.\d+|\d+", ardString)
        h = dataArray[0]
        t = dataArray[1]
        humid.append(h)
        temp.append(t)
        drawnow(plot)
        plt.pause(5)

        cnt = cnt+1

        if cnt == 60:
            now = datetime.datetime.now()
            plt.suptitle('Status for ' + str(now.month) + '/' + str(now.day) +
                    '/' + str(now.hour-1) +':'+str(now.minute) + '-' + str(now.hour)+':' +
                    str(now.minute))
            plt.savefig(str(now.month) + '-' + str(now.day) + '-' + str(now.hour))
            cnt = 0 
            h, t = [], []
