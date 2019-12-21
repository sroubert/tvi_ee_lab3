'''
*Author: Sebastian Roubert Martinez
*Last Date Modified: 12/17/19

*The following script allows user to control AxiDraw3 with RPi Motor Hat.
*Specifically, it takes an array of line data (formatted [[x11,y11,x12,y12],[x21,y21,x22,y22],...)
*and plots the lines.
'''

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time
import numpy as np
kit = MotorKit()
kit.stepper2.release()
kit.stepper1.release()


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
                #print("hi") #always step  in x
                if ( x > 0): xForward()
                if ( x < 0): xBackward()
                #check when step in y
                if ( (i % ratio)== 0 ): #ASK STUDENTS WHAT TO PUT HERE
                        if ( y > 0 ): yForward()
                        if ( y < 0 ): yBackward()



'''
*if xMove or yMove are zero
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


    if ( abs( yMove ) >= abs( xMove ) ):
        ratio = round(abs( yMove / xMove) )
        loopY(ratio,yMove,xMove)

    
    if ( abs( xMove ) > abs( yMove ) ):
            ratio = round(abs( xMove / yMove) )
            loopX(ratio,yMove,xMove)

'''
******STUDENT*******
'''

'''
PUT YOUR LINES HERE
'''


lines =np.array([[134,222,182,221],\
[84,102,87,81],\
[169,43,206,43],\
[103,45,149,45],\
[177,216,195,216],\
[58,1,67,1],\
[155,217,173,217],\
[77,151,81,118],\
[146,1,156,1],\
[152,46,179,46]])




'''
#pseudo  code
lastPos = 0,0
for line in lines
    go to x1,y1 from lastPos
    put down servo
    go to x2,y2 from x1,y1
    bring up servo
    lastPos = x2, y2
'''

#extract
x1_all = lines[:,0]
y1_all = lines[:,1]
x2_all = lines[:,2]
y2_all = lines[:,3]

#comes inverted to switch the y's


'''
*scale to gantry range
'''

xRange = 20
yRange = 15

picWidth = 400
picHeight = 300

#mirror about middle axis parallel to the x-axis
y1_all = [ -y+picHeight for y in  y1_all]
y2_all = [ -y+picHeight for y in  y2_all]


#to be measured by students
stepsPerCm = 50

#scale and round for iterable numbers
x1_all =  stepsPerCm*(xRange/picWidth) * x1_all 
x2_all =  stepsPerCm*(xRange/picWidth) * x2_all 
y1_all = stepsPerCm*(yRange/picHeight) * np.asarray(y1_all) 
y2_all = stepsPerCm*(yRange/picHeight) * np.asarray(y2_all) 




#extract the number of rows in lines object.
numLines = np.size(lines,0)

#move to first point
deltaYtoStart = (y1_all[0] - 0) 
deltaXtoStart = (x1_all[0] - 0) #*stepsPerCm

moveLine(int(deltaXtoStart), int(deltaYtoStart))
print(f"point 1= ( {x1_all[0]}, {y1_all[0]} )") 
input("here")

#accumulate error from int, check later if helps with shallow line angles
xError = 0
yError = 0

for i in range(numLines):
    input("put down servo")
    
    deltaY_draw = ( int(y2_all[i] - y1_all[i]) ) #*stepsPerCm
    deltaX_draw = ( int(x2_all[i] - x1_all[i]) ) #*stepsPerCm
    
    
    
    print((deltaY_draw))
    print((deltaX_draw))
    
    #moveLine(deltaX_draw ,deltaY_draw)
    moveLine((deltaX_draw),(deltaY_draw))
    
    input("bring up servo")
    
    #check if at end
    if (i==numLines-1):
        print("all lines drawn")
    else: #move to next point
        deltaY_nextPoint = ( int(y1_all[i+1] - y2_all[i]) ) #*stepsPerCm
        deltaX_nextPoint = ( int(x1_all[i+1] - x2_all[i]) ) #*stepsPerCm
        moveLine(int(deltaX_nextPoint), int(deltaY_nextPoint))


'''
DO NOT CHANGE, motors must release to stop current draw
'''
kit.stepper2.release()
kit.stepper1.release()

