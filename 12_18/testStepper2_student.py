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
input("about to test stepper two, forward, single coil")
for i in range(200):
   #
   #STUDENT
   #CODE
   #HERE
   #

#stepper 1 behavior FORWARD: movement in +Y and +X
input("about to test stepper two, backward, single coil")
for i in range(200):
   #
   #STUDENT
   #CODE
   #HERE 
   #



'''
Do the exact same as above but with double coil. Please comment on differences.
'''

#
#CODE
#HERE
#
#

kit.stepper1.release()
kit.stepper2.release()




