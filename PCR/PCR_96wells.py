#		******    INSTRUCTIONS    ******
#
#	1. This PCR protocol ONLY makes Master Mix containing:
#			dntps
#			polymerase
#			reaction buffer
#			water
#		and distrbute it into 96 wells. 
#		DNA template and Primers will be added through ECHO.
#	2. Please place the necessary items according to the map as shown below		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    MATERIALS NEEDED    ******
#
#	1. 20 tube rack 			X 1
#	2. 200ul tiprack 			X 1
#	3. 96 well plate 			X 1
#	4. trash container 			X 1
#	5. dntps
#	6. Polymerase
#	7. Reaction Buffer
#	8. Water
#	9. Empty tube (to be placed in 1.) for Master Mix
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    20 tube rack    ******
#          A               B               C               D               
#    _______________________________________________________________
#   |               |               |               |               |
#   |               |               |               |               |  5
#   |               |               |               |               |
#   |_______________________________________________________________|
#   |               |               |               |               |
#   |               |               |               |               |  4 
#   |               |               |               |               |
#   |_______________________________________________________________|
#   |               |               |               |               |
#   |               |               |               |               |  3
#   |               |               |               |               |
#   |_______________________________________________________________|
#   |               |               |               |               |
#   |     dntps     |  polymerase   |   Reaction    |    water      |  2
#   |               |               |    Buffer     |               |  
#   |_______________________________________________________________|
#   |               |               |               |               |
#   |               |  Master Mix   |               |               |  1 
#   |               | prepared here |               |               |
#   |_______________________________________________________________|
# 
#
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

from opentrons import containers, instrument, robot
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environemnt.get_path('CALIBRATIONS_FILE'))

robot.home()

tube_rack = containers.load('tube-rack-2ml', 'C3', 'tube_rack')
plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')

m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200-rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m2 = instruments.Pipette(
	name = "m2",
	trash_container = trash2,
	tip_racks = [m200rack2],
	min_volume = 10,
	max_volume = 200,
	axis = "a",
	channels = 1)

#for a 96 well plate
print('Preparing PCR Master Mix...')
#dntps 38.4ul #
m2.transfer(39, tube_rack.wells('A2'), tube_rack.wells('B1'), trash=True)
#polymerase 19.2ul #
m2.transfer(19, tube_rack.wells('B2'), tube_rack.wells('B1'), trash=True)
#reaction buffer 384ul#
m2.transfer(384, tube_rack.wells('C2'), tube_rack.wells('B1'), trash=True)
#water 1440ul#
m2.transfer(1440, tube_rack.wells('D2'), tube_rack.wells('B1'), new_tip='never')
m2.mix(8)
m2.drop_tip(trash2)

print('Master Mix is ready.')
print('Distributing Master Mix...')
m2.distribute(20, tube_rack.wells('B1'), plate2, trash=True)

print('Distribution is completed. Please transfer plate at C2 to ECHO as Destination Plate.')
print('Remove everything from Opentrons, discard if necessary. Thank you :)')
