from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time 
kit = MotorKit()
kit.stepper2.release()
kit.stepper1.release()

 #line is x1, y1, x2, y2

#x_diff = x2 - x1
x_diff = -10
#y_diff = y2 - y1
y_diff = -2

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

if (yMove==0):
	for i in range( abs( xMove )):
		if (xMove > 0): xForward()
		if (xMove < 0): xBackward()
	kit.stepper2.release()
	kit.stepper1.release()
	exit() #this ends the python script

if (xMove==0):
        for i in range( abs( yMove )):
                if (yMove > 0): yForward()
                if (yMove < 0): yBackward()
        kit.stepper2.release()
        kit.stepper1.release()
        exit() #this ends the python script


'''
*loop through steps
'''
#loop over y
if ( abs( yMove ) > abs( xMove ) ):
	ratio = round(abs( yMove / xMove) )
	loopY(ratio,yMove,xMove)

#loop over x
if ( abs( xMove ) > abs( yMove ) ):
        ratio = round(abs( xMove / yMove) )
        loopX(ratio,yMove,xMove)



kit.stepper2.release()
kit.stepper1.release()

