from opentrons import robot, instruments, containers

source_plate = containers.load('trough-12row', 'B2', 'source_plate')
plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')
elute_plate = containers.load('96-PCR-flat', 'C1', 'elute_plate')
mag_deck= instruments.Magbead(name='mag_deck')
m200rack2 = containers.load('tiprack-200ul', 'A2', 'm200-rack2')

trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack2],
	min_volume = 10,
	max_volume = 200,
	axis = "a",
	channels = 8)

#for a 96 well plate, 20ul Sample Reaction Volume
#addition of AMPure XP -> total volume in each well = 56ul
for row in plate2.rows():
	m200.transfer(36, source_plate('A1'), row, mix_after=(10,40), new_tip='always', trash=True)

for c in robot.commands():
	print(c)
