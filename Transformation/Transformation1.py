# for instructions, please refer to TransformationMASTER.py

from opentrons import containers, instruments, robot

source_plate = containers.load('96-PCR-flat', 'B2', 'source_plate')
cold_plate = containers.load('96-PCR-flat', 'C2', 'cold_plate')
hot_plate = containers.load('96-PCR-flat', 'C1', 'hot_plate')
m2rack2 = containers.load('tiprack-10ul', 'A2', 'm2rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m2 = instruments.Pipette(
	name = "m2",
	trash_container = trash2,
	tip_racks = [m2rack2],
	min_volume = 0.2,
	max_volume = 2,
	axis = "a",
	channels = 8)

i=0
for row in cold_plate.rows():
	m2.transfer(2, source_plate(i), row, mix_after=(4, 30), new_tips='always')
	i += 1

m2.delay(minutes=29)

robot.run()
