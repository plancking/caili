from math import *

IZZ=95109333.33/(1e12)
SZ=348800/(1e9)
b=6e-3
A=5680/(1e6)
EX=2.1e11
ymax=0.15
DENS=7.85e3
ACEL=9.8
tmp=input("请输入学号:")
length=int(tmp[-3:])
if length>=100:
    force=length*10
    length=length*10/1000
else:
    force=length*100
    length=length*100/1000

q=DENS*A*ACEL
fs=force+q*length
ms=force*length+q*length*length/2
sigma=ms*ymax/IZZ/(1e6)
tao=fs*SZ/b/IZZ/(1e6)
sigma4=sqrt(sigma*sigma+3*tao*tao)
print("sigma={:.6}MPa,tao={:.6}MPa,sigma4={:.6}MPa".format(sigma,tao,sigma4))
disp=force*length*length*length/3/EX/IZZ+q*length*length*length*length/8/EX/IZZ
disp=disp*1000
print("disp={:.6}mm".format(disp))
