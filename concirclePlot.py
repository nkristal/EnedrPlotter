# -*- coding: utf-8 -*-
"""
Created on Sat Nov 06 21:54:08 2021

@author: Nir Kristal
"""
import numpy as np
from PIL import Image
import sys

cx = 0.0
cy = 0.0
cz = 0.0


penUpZ = 15.0
penDnZ = 13.2


def putCircle(x, y, size=1, edges=11):
    """
    prints the gcode for a circle around (x,y) to size,
    calls for smaller circles.
     * add sanity checks for size?
     f"Hello, {name}. You are {age}." only in python 3.6
    """
    print(";Circle " + str(x) +" "+ str(y) +" "+ str(size) +" "+ str(edges))
    
    angle = np.linspace( 0 , 2 * np.pi , edges )
    cx = x + size * np.cos( angle )
    cy = y + size * np.sin( angle ) 
 
    travelTo(cx[0], cy[0])
    penDn()   
    for i, j in zip(cx ,cy):
        print("G1 X" +str(i) + " Y" + str(j) + " F1600")

def putConcircle(x, y, size, edges = 11):
    if size>2:
        putConcircle(x, y, size-1, edges)
    putCircle(x, y, size, edges)
    
        
def travelTo(x, y):
    penUp()
    print("G0 X" +str(x) + " Y" + str(y) + " F6000")

def penUp():
    print("G0 Z" + str(penUpZ) + " F6000")

def penDn():
    print("G0 Z" + str(penDnZ) + " F1600")

def installPen():
    calX = 50
    calY = 40
    if cz != penUpZ :
        penUp()
    print("G1 X" +str(calX) + " Y" + str(calY) + " F1600")
    penDn()
    print("M0")
    penUp()
    print

def startGCode():
    print('G28 X Y Z')
    penUp()
    penUp()
    installPen()

def endGCode():    
    print    
    penUp()
    print("G1 X50.0 Y40.0 F6000")
    print('G28 X')

    
sys.stdout = open("star1_1.gcode", "w")

im = np.array(Image.open('star1.png').convert('L')) #you can pass multiple arguments in single line
#print(type(im))
#print(im)
print(im[1,:])
im = np.floor(255 - im)
print(im[1,:])
im /= im.max()/10.0
print(im[1,:])
#Image.fromarray(im).save("ella18_out.png")
#np.savetxt("foo.csv", im, delimiter=",")

rows = im.shape[0]
cols = im.shape[1]
#print rows
#print cols

ox = 55
oy = 45
fox = 55
foy = 45
step = 10

startGCode()
for i in range(0, rows):
    for j in range(0, cols):
        putConcircle(ox, oy, im[i,j]/2)
        #print ox, oy, im[i,j]
        ox += step
    oy += step
    ox = fox

endGCode()
    
sys.stdout.close()
        
#gr_im= Image.fromarray(im).save('ella1_outt.png')


#startGCode()
#putCircle(140, 135, 2)



