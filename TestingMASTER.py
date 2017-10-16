from opentrons import robot, containers, instruments
from opentrons.util import environment
import os


robot.connect('/dev/ttyACM0')


environment.refresh()
print(environment.get_path('CALIBRATIONS_FILE'))



robot.home()

exec(open('/home/changlab/Desktop/Opentrons/Testing2.py').read())
input('Press enter to continue...')

robot.reset()
robot.home()

exec(open('/home/changlab/Desktop/Opentrons/Testing1.py').read())
