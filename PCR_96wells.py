#		******    INSTRUCTIONS    ******
#
#	1. This PCR protocol ONLY distributes Master Mix containing:
#			dntps
#			polymerase
#			reaction buffer
#			water
#		into 96 wells. 
#		DNA template and Primers will be added through ECHO.
#	2. Please place the necessary items according to the map as shown below		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    MATERIALS NEEDED    ******
#
#	1. 20 tube rack 			X 1
#	2. 200ul tiprack 			X 1
#	3. 96 well plate 			X 1
#	4. trash container 			X 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       ******      MAP -- PHYSICAL LAYOUT OF OPENTRONS   *******
#
#          A               B               C               D                E
#    _______________________________________________________________________________
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |               |               |  20 tube rack |               |               |  3
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |     trash     |               |
#   |               | 200ul tiprack | 96 well plate |   container   |               |  2 
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |               |               |               |               |               |  1
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|

from opentrons import containers, instruments, robot
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environment.get_path('CALIBRATIONS_FILE'))

robot.home()
tuberack20 = containers.create('tuberack20', grid=(4, 5), spacing =(18,21), diameter = 10, depth = 33)
abwell = containers.create('abwell', grid=(8, 12), spacing = (9, 9), diameter = 5.4, depth= 14.8)
tube_rack = containers.load('tuberack20', 'C3', 'tube_rack')
plate2 = containers.load('abwell', 'C2', 'plate2')

m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200-rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack2],
	min_volume = 10,
	max_volume = 200,
	axis = "a",
	channels = 8)

print('Distributing Master Mix...')

plate_a=[]
i=0
for col in plate2.cols():
	for i in range(12):
		plate_a.append(col.wells(i, length=1, step=1))
		i += 1

m200.pick_up_tip(m200rack2.well('A1'))
m200.distribute(20, tube_rack.wells('A1'), plate_a, trash=True)

print('Distribution is completed. Please transfer plate at C2 to ECHO as Destination Plate.')
print('Remove everything from Opentrons, discard if necessary. Thank you :)')

robot.run()