from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time
import numpy as np
kit = MotorKit()
kit.stepper2.release()
kit.stepper1.release()

'''
PUT YOUR LINES HERE
'''

lines=np.array([[110,72,121,62],\
[147,39,172,17],\
[149,38,152,35],\
[100,80,103,77],\
[20,131,35,130],\
[162,66,166,66],\
[210,73,213,73]])

'''
#pseudo code
lastPos = 0,0
for line in lines
    go to x1,y1 from lastPos
    put down servo
    go to x2,y2 from lastPos
    bring up servo
    lastPos = x2, y2
'''




#x_diff = x2 - x1
x_diff = 10
#y_diff = y2 - y1
y_diff = 2

#to be measured by students
stepsPerCm = 50

yMove = y_diff*50
xMove = x_diff*50



'''
DO NOT CHANGE: Define basic move functions
'''
def yForward():
   kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
   kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)

def yBackward():
   kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
   kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)


def xForward():
   kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
   kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

def xBackward():
   kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
   kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)


'''
*loop functions
'''

def loopY(ratio,y,x):
    for i in range( abs(y) ):
        #always step  in y
        if ( y > 0): yForward()
        if ( y < 0): yBackward()
        #check when step in X
        if ( (i % ratio)== 0 ): #ASK STUDENTS WHAT TO PUT HERE
            if ( x > 0 ): xForward()
            if ( x < 0 ): xBackward()

def loopX(ratio,y,x):
        for i in range( abs(x) ):
                print("hi") #always step  in x
                if ( x > 0): xForward()
                if ( x < 0): xBackward()
                #check when step in y
                if ( (i % ratio)== 0 ): #ASK STUDENTS WHAT TO PUT HERE
                        if ( y > 0 ): yForward()
                        if ( y < 0 ): yBackward()



'''
*if there xMove or yMove are zero
'''
def moveLine(xMove,yMove):
    if (yMove==0):
        for i in range( abs( xMove )):
            if (xMove > 0): xForward()
            if (xMove < 0): xBackward()
        kit.stepper2.release()
        kit.stepper1.release()
        return #this ends the python function

    if (xMove==0):
        for i in range( abs( yMove )):
                if (yMove > 0): yForward()
                if (yMove < 0): yBackward()
        kit.stepper2.release()
        kit.stepper1.release()
        return #this ends the python function


    if ( abs( yMove ) > abs( xMove ) ):
        ratio = round(abs( yMove / xMove) )
        loopY(ratio,yMove,xMove)

    
    if ( abs( xMove ) > abs( yMove ) ):
            ratio = round(abs( xMove / yMove) )
            loopX(ratio,yMove,xMove)



kit.stepper2.release()
kit.stepper1.release()

