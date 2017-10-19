from opentrons import robot, containers, instruments
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environemnt.get_path('CALIBRATIONS_FILE'))

robot.home()
exec(open('Transformation1.py').read())
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('Transformation2.py').read())
