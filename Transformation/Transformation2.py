# for instructions, please refer to TransformationMASTER.py

from opentrons import containers, instruments, robot

plate2 = containers.load('96-PCR-flat', 'B1', 'plate2')
cold_plate = containers.load('96-PCR-flat', 'C2', 'cold_plate')
hot_plate = containers.load('96-PCR-flat', 'C1', 'hot_plate')
media = containers.load('point', 'C3', 'media')
m1000rack2 = containers.load('tiprack-1000ul', 'B1', 'm1000rack2')
m1000rack3 = containers.load('tiprack-1000ul', 'B3', 'm1000rack3')
m1000rack4 = containers.load('tiprack-1000ul', 'A1', 'm1000rack4')
trash2 = containers.load('point', 'D2', 'trash2')

m1000 = instruments.Pipette(
	name = "m1000",
	trash_container = trash2,
	tip_racks = [m1000rack2, m1000rack3, m1000rack4],
	min_volume = 100,
	max_volume = 1000,
	axis = "a",
	channels = 8)

i=0
for row in hot_plate.rows():
	m1000.transfer(52, cold_plate.rows(i), row, new_tip='always', trash=False)
	i +=1

for row in plate2.rows():
	m1000.transfer(52, hot_plate.rows(i), row, new_tip='always')
	i += 1

for row in plate2.rows():
	m1000.transfer(950, media('A1'), row, new_tip=('always'))

robot.run()
