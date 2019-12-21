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


input("about to test stepper two, forward, single coil")
#expected result, movement in -x and -y
for i in range(200):
   #fill in below
   kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)

input("about to test stepper two, backward, single coil")
#expected result, movement in +x and +y
for i in range(200):
   #fill in below
   kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)


'''
Do the exact same as above but with double coil. Please comment on differences.
'''
#differnece, behavior is much smoother throughout, quieter


#expected result, movement in -x and -y
input("about to test stepper two, forward, double coil")
for i in range(200):
   #fill in below
   kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)

#expected result, movement in +x and +y
input("about to test stepper two, backward, double coil")
for i in range(200):
   #fill in below
   kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)


kit.stepper1.release()
kit.stepper2.release()




