from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time 
#hi
kit = MotorKit()
kit.stepper2.release()
kit.stepper1.release()

xDistance = 4 #cm
yDistance = 2 #cm

stepsPerCm = 50

loopNumX = xDistance*stepsPerCm
loopNumY = yDistance*stepsPerCm


'''DO NOT CHANGE: Define basic move functions'''
def xForward(loopNum):
    for i in range(loopNum):
       kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
       kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

def yForward(loopNum):
        for i in range(loopNum):
           kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
           kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)



'''Calibrate'''
xForward(loopNumX)

yForward(loopNumY)



kit.stepper2.release()
kit.stepper1.release()


