# For instructions, please refer to ExtractingDNA_MASTER.py

from opentrons import robot, instruments, containers

plate384 = containers.create('plate384', grid=(16,24), spacing=(4.5,4.5), diameter=3.87, depth=9)

source_plate = containers.load('trough-12row', 'B2', 'source_plate')
plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')
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

#addition of 40ul elution buffer
print('Adding Elution Buffer')
for row in plate2.rows:
	m200.transfer(40, source_plate('A5'), row, mix_after=(10, 35), new_tip='always', trash=False)
m200.delay(120)
#separate magnetic beads from mixture
print('Separating Magnetic Beads')
mag_deck.engage()
m200.delay(60)
i=0
for row in elute_plate.rows():
	m200.transfer(38, plate2.rows(i), row, new_tip='always', trash=True)
	i += 1

for c in robot.commands():
	print(c)

robot.run()
