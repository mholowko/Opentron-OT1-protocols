#               INSTRUCTIONS
#	1. This Transformation Protocol closely follows the protocol found on
#		https://www.neb.com/protocols/2012/05/21/transformation-protocol
#	2. Ensure that files:
#			TransformationMASTER.py
#			Transformation1.py
#			Transformation2.py
#		are in the same folder before executing
#	3. Please place the necessary items according to the map shown below. 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 		******    MATERIAL NEEDED    ******
#
#	1. 2ul Tiprack 				X 1
#	2. 1000ul Tiprack 			X 1
#	3. Container containing Media
#	6. 96 well plate 			X 1
#	7. Trash Container 			X 1
#	8. Cold Deck 				X 1
#	9. Heat Deck 				X 1
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#      ******   MAP -- PHYSICAL LAYOUT OF OPENTRONS   ******
# 
#          A               B               C               D                E
#    _______________________________________________________________________________
#   |               |               |               |               |               |
#   |               |               |     media     |               |               |
#   |               | tiprack-200ul |   container   |               |               |  3
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |     trash     |               |
#   | tiprack-200ul | 20-tube-rack  | 96 well plate |   container   |               |  2 
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |               |               |               |               |               |  1
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#

from opentrons import instruments, robot, containers 
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environment.get_path('CALIBRATIONS_FILE'))

robot.home()
exec(open('Transformation1.py').read())
print('Part (1/2) of Transformation is completed')
print('Please change pipette to m1000 before proceeding')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('Transformation2.py').read())
print('Part (2/2) of Transformation is completed')
print('Protocol is completed.')
print('Remove everything from Opentrons, discard if necessary. Thank you :)')