#     ******    INSTRUCTIONS    ******
#
#	1. This Transformation Protocol closely follows the protocol found on
#		  https://www.neb.com/protocols/2012/05/21/transformation-protocol
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
#	2. 1000ul Tiprack 			X 3
#	3. Container containing Media
#	4. 96 well plate from Gibson Assembly
#	5. 96 well plate containing Competent Cells in each well
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
#   |               |tiprack-1000ul |   container   |               |               |  3
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |Competent Cells|               |               |
#   |               | 96 well plate | 96 well plate |     trash     |               |
#   |  tiprack-2ul  | obtained from |   on top of   |   container   |               |  2 
#   |               |Gibson Assembly|   COLD DECK   |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               | 96 well plate |               |               |
#   |tiprack-1000ul |tiprack-1000ul |   on top of   |               |               |  1
#   |               |               |   HEAT DECK   |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#

from opentrons import instruments, robot, containers 
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environemnt.get_path('CALIBRATIONS_FILE'))

robot.home()
exec(open('Transformation1.py').read())
print('Part (1/2) of Transformation is completed')
print('Please change pipette to m1000 before proceeding')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('Transformation2.py').read())
print('Part (2/2) of Transformation is completed')
print('Protocol is completed. Please proceed to spread')
print('cells and ligation mixture, from each well, onto plates.')
print('Remove everything from Opentrons, discard if necessary. Thank you :)')
