from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time 
#hi
kit = MotorKit()
kit.stepper2.release()
kit.stepper1.release()

loopNum = 200

'''DO NOT CHANGE: Define basic move functions'''
def yForward(loopNum):
	for i in range(loopNum):
	   kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
	   #time.sleep(pause)
	   kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
	   #time.sleep(pause)

def yBackward(loopNum):
        for i in range(loopNum):
           kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
           #time.sleep(pause)
           kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
           #time.sleep(pause)



'''Movement y'''
#yBackward(loopNum)
#input("measure")
yForward(loopNum)
input("measure")

kit.stepper2.release()
kit.stepper1.release()


