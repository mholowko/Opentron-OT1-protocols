from opentrons import containers, robot, instruments 

source_plate = containers.load('96-PCR-flat', 'B2', 'source_plate')
cold_plate = containers.load('96-PCR-flat', 'C2', 'cold_plate')
hot_plate = containers.load('96-PCR-flat', 'C1', 'hot_plate')
media = container.load('point', 'C3', 'media')
m200rack2 = containers.load('tiprack-200ul', 'A2', 'm200rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack2],
	min_volume = 0,
	max_volume = 1000,
	axis = "a",
	channels = 8)

i=0
for row in cold_plate.rows():
	m200.transfer(2, source_plate.rows(i), row, mix_after(3, 10), new_tip='always')
	i += 1

m200.delay(minutes=30)

for row in hot_plate.rows():
	m200.transfer(52, cold_plate.rows(i), row, new_tip='always')
	i +=1
m200.delay(30)

for row in hot_plate.rows():
	m200.transfer(950, media, row, new_tip='always')

m200.delay(minutes=60)
