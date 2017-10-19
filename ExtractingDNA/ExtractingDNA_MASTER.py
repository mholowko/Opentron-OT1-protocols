from opentrons import robot, containers, instruments
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environemnt.get_path('CALIBRATIONS_FILE'))

robot.home()

print('There are 4 parts of Transformation Protocol')
exec(open('ExtractingDNA1.py').read())
print('Part 1 of Transformation is completed.')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('ExtractingDNA2.py').read())
print('Part 2 of Transformation is completed.')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('ExtractingDNA3.py').read())
print('Part 3 of Transformation is completed.')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('ExtractingDNA4.py').read())
print('Part 4 of Transformation is completed.')
