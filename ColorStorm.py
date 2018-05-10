import os
from numpy import*
from PIL import Image
import adb
import time
def RGBAtoH(RGBA):
    return RGBA[0]*1000000+RGBA[1]*1000+RGBA[2]

#print im.getpixel((400,400))
#print RGBAtoH(im.getpixel((400,400)))

def PLAY(n):    #there is n lines and n rols
    adb.screencap("test.png")
    im = Image.open("test.png")
    x0,y0=41,535
    box=(x0,y0,1041,1535)
    part=im.crop(box)
    #part.show()
    #print part.size[0],part.size[1]

    line=rol=n
    array = [['*' for i in range(line)] for i in range(rol)]

    dl=500/line

    for i in range(line):
        for j in range(rol):
            color = RGBAtoH(part.getpixel(((2*j+1)*dl,(2*i+1)*dl)))
            array[i][j] = color
    print array

    if (array[0][0]==array[0][1]):color=array[0][0]
    else:color=array[1][1]

    for i in range(line):#find and tap
        for j in range(rol):
            temp = RGBAtoH(part.getpixel(((2*j+1)*dl,(2*i+1)*dl)))
            if temp!=color:
                adb.tap(x0+(2*j+1)*dl,y0+(2*i+1)*dl)
                print "tap:",(2*j+1)*dl,(2*i+1)*dl
                break
            if temp!=color:break
            
    im.close()
    part.close()



k=0
while(1):
    if k<110:PLAY(k/10+2)
    else:PLAY(12)
    k=k+1
    time.sleep(0.3)
    while k==233:raw_input()
