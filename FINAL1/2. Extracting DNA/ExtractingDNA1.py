# For instructions, please refer to ExtractingDNA_MASTER.py

from opentrons import robot, instruments, containers

plate384 = containers.create('plate384', grid=(16,24), spacing=(4.5,4.5), diameter=3.8, depth=10.91)
abwell = containers.create('abwell', grid=(8, 12), spacing = (9.025, 9.025), diameter = 5.5, depth= 20)

source_plate = containers.load('trough-12row', 'B2', 'source_plate')
plate2 = containers.load('abwell', 'C2', 'plate2')
elute_plate = containers.load('plate384', 'C1', 'elute_plate')
mag_deck= instruments.Magbead(name='mag_deck')
m200rack2 = containers.load('tiprack-200ul', 'A2', 'm200-rack2')
m200rack3 = containers.load('tiprack-200ul', 'A1', 'm200-rack3')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack2, m200rack3],
	min_volume = 10,
	max_volume = 200,
	axis = "a",
	channels = 8)

#for a 96 well plate, 20ul Sample Reaction Volume
#addition of AMPure XP -> total volume in each well = 56ul
for i in range(12):
	m200.transfer(36, source_plate('A1'), plate2.rows(i), mix_after=(10,40), new_tip='always', trash=True)
	
#separate beads for 2min, leave behind 5~6ul supernatant
print('Separating beads for 2min')
mag_deck.engage()
m200.delay(120)
for i in range(12):
	m200.transfer(50, plate2.rows(i), trash2, new_tip='always', trash=True)

robot.run()