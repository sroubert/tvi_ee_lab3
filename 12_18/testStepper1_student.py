from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time 

kit = MotorKit()

kit.stepper1.release()
kit.stepper2.release()

"""
* To test:
* stepper single coil
"""

#stepper 1 behavior FORWARD: movement in -Y and -X
input("about to test stepper one, forward, single coil")
for i in range(200):
    kit.stepper1.onestep(direction=stepper.FORWARD, style = stepper.SINGLE)
   
   #

#stepper 1 behavior FORWARD: movement in +Y and +X
input("about to test stepper one, backward, single coil")
for i in range(200):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style = stepper.SINGLE)   #



'''
Do the exact same as above but with double coil. Please comment on differences.
'''
input("about to test stepper one, forward, double coil")
for i in range(200):
    kit.stepper1.onestep(direction=stepper.FORWARD, style = stepper.DOUBLE)
    
input("about to test stepper one, backward, double coil")
for i in range(200):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style = stepper.DOUBLE)  
#
#CODE
#HERE
#
#

kit.stepper1.release()
kit.stepper2.release()




