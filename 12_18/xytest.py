from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time 

kit = MotorKit()
kit.stepper2.release()

pause =0 #0.0001

for i in range(200):
   kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
   time.sleep(pause)
   kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
   time.sleep(pause)

kit.stepper1.release()
kit.stepper2.release()

input("-X: S1 = F, S2 = F")

for i in range(200):
   kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
   time.sleep(pause)
   kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
   time.sleep(pause)

kit.stepper1.release()
kit.stepper2.release()

input("-Y: S1 = F, S2 = B")

for i in range(200):
   kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
   time.sleep(pause)
   kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
   time.sleep(pause)

kit.stepper1.release()
kit.stepper2.release()

input("+X: S1 = B, S2 = B")

for i in range(200):
   kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
   time.sleep(pause)
   kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
   time.sleep(pause)

kit.stepper1.release()
kit.stepper2.release()

input("+Y S1 = B, S2 = F")
