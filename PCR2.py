from opentrons import containers, instruments, robot
from opentrons.util import environment
import os

robot.connect('/dev/ttyACM0') 
environment.refresh()
print(environment.get_path('CALIBRATIONS_FILE'))

robot.home()
tuberack20 = containers.create('tuberack20', grid=(4, 5), spacing =(18,21), diameter = 10, depth = 33)
abwell = containers.create('abwell', grid=(8, 12), spacing = (9.025, 9.025), diameter = 5.5, depth= 20)
tube_rack = containers.load('tuberack20', 'C3', 'tube_rack')
plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')
GEplate = containers.load('abwell', 'C1', 'GEplate')
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


m200.pick_up_tip(m200rack2.well('A1'))
m200.distribute(20, tube_rack.wells('A1'), plate_a, trash=True)
i=0
for row in GEplate.rows():
   m200.transfer(25, plate2.rows(i), row, new_tip='always', trash=True)
    i +=1

robot.run() 
