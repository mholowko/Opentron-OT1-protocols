#   ******    INSTRUCTIONS    ******
#
#	1. Ensure that files:
#			ExtractingDNA_MASTER.py
#			ExtractingDNA1.py
#			ExtractingDNA2.py
#			ExtractingDNA3.py
#			ExtractingDNA4.py
#		are in the same folder before executing. 
#	2. Connect MAG DECK to Opentrons
#		Please refer to https://support.opentrons.com/hardware-questions/hardware-modules/magdeck		
#	3. Place place necessary items according to the map as shown below
#	4. If tiprack has ran out of tips before the end of DNA Extraction Protocol, 
#		please replace them with new ones at the same location. 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    MATERIALS NEEDED    ******
#
#	1. 200ul tiprack 					X 8
#	2. 12-row trough 					X 1
#	3. 96 well plate from Gel E.		X 1
#	4. 384 well palte 					x 1
#	5. trash container 					X 1
#	6. Ampure XP
#	7. Ethanol
#	8. Elution Buffer
#	9. Magnetic Deck
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    12-ROW TROUGH    *******
#	 __________________________
#	|                          | 12
#	|--------------------------|
#	|                          | 11
#	|--------------------------|
#	|                          | 10
#	|--------------------------|
#	|                          |  9
#	|--------------------------|
#	|                          |  8
#	|--------------------------|
#	|                          |  7
#	|--------------------------|
#	|                          |  6
#	|--------------------------|
#	|      Elution Buffer      |  5     Add this after completing Part (3/4)
#	|--------------------------|
#	|                          |  4
#	|--------------------------|
#	|         Ethanol          |  3     Add this after completing Part (1/4)
#	|--------------------------|
#	|                          |  2
#	|--------------------------|
#	|         Ampure XP        |  1     Add this before starting protocol 
#	 --------------------------
#
#       ******      MAP -- PHYSICAL LAYOUT OF OPENTRONS   ***********
#
#          A               B               C               D                E
#    _______________________________________________________________________________
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |               |               |               |               |               |  3
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               | 96 well plate |               |               |
#   |               |               |  from Gel E.  |     trash     |               |
#   | tiprack-200ul | 12-row trough |   on top of   |   container   |               |  2 
#   |               |               |   MAG DECK    |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   | tiprack-200ul |               |384 well plate |               |               |  1
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|


from opentrons import containers, instrument, robot
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environemnt.get_path('CALIBRATIONS_FILE'))

robot.home()

print('There are 4 parts to DNA Extraction Protocol')
exec(open('ExtractingDNA1.py').read())
print('Part (1/4) of DNA Extraction is completed.')
print('Please place Ethanol in A3 of 12 row trough at B2 before proceeding.')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('ExtractingDNA2.py').read())
print('Part (2/4) of DNA Extraction is completed.')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('ExtractingDNA3.py').read())
print('Part (3/4) of DNA Extraction is completed.')
print('Please place Elution Buffer in A5 of 12 row trough at B2 before proceeding.')
input('Press enter to continue...')
robot.reset()
robot.home()
exec(open('ExtractingDNA4.py').read())
print('Part (4/4) of DNA Extraction is completed.')
print('DNA Extraction is completed. Please take plate containing extracted DNA at C1')
print('& remove all items from Opentrons, discard if necessary. Thank you :)')
