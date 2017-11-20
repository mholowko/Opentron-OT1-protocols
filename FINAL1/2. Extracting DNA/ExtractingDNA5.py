# For instructions, please refer to ExtractingDNA_MASTER.py

from opentrons import robot, instruments, containers

plate384 = containers.create('plate384', grid=(16,24), spacing=(4.5,4.5), diameter=3.8, depth=10.91)
abwell = containers.create('abwell', grid=(8, 12), spacing = (9.025, 9.025), diameter = 5.5, depth= 20)

source_plate = containers.load('trough-12row', 'B2', 'source_plate')
plate2 = containers.load('abwell', 'C2', 'plate2')
elute_plate = containers.load('plate384', 'C1', 'elute_plate')
mag_deck= instruments.Magbead(name='mag_deck')
m200rack2 = containers.load('tiprack-200ul', 'B3', 'm200-rack2')
m200rack3 = containers.load('tiprack-200ul', 'B1', 'm200-rack3')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack2, m200rack3],
	min_volume = 10,
	max_volume = 200,
	axis = "a",
	channels = 8)


for i in range(12):
	m200.transfer(200, plate2.rows(i), trash2, new_tips='always', trash=True)
m200.delay(30)
mag_deck.disengage()
#addition of 40ul elution buffer
print('Adding Elution Buffer')
for i in range(12):
	m200.transfer(40, source_plate('A5'), plate2.rows(i), mix_after=(10, 35), new_tip='always', trash=False)
m200.delay(120)