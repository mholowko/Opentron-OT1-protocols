from opentrons import robot, instruments, containers

source_plate = containers.load('trough-12row', 'B2', 'source_plate')
plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')
elute_plate = containers.load('96-PCR-flat', 'C1', 'elute_plate')
mag_deck= instruments.Magbead(name='mag_deck')
m200rack2 = containers.load('tiprack-200ul', 'A2', 'm200-rack2')
m200rack3 = containers.load('tiprack-200ul', 'A1', 'm200-rack3')
m200rack4 = containers.load('tiprack-200ul', 'A3', 'm200-rack4')
m200rack5 = containers.load('tiprack-200ul', 'B1', 'm200-rack5')
m200rack6 = containers.load('tiprack-200ul', 'B3', 'm200-rack6')
m200rack7 = containers.load('tiprack-200ul', 'C1', 'm200-rack7')
m200rack8 = containers.load('tiprack-200ul', 'C3', 'm200-rack8')
m200rack9 = containers.load('tiprack-200ul', 'D1', 'm200-rack9')
m200rack10 = containers.load('tiprack-200ul', 'D3', 'm200-rack10')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack2, m200rack3, m200rack4,m200rack5,m200rack6,m200rack7,m200rack8,m200rack9,m200rack10],
	min_volume = 10,
	max_volume = 200,
	axis = "a",
	channels = 8)

plate_a = []
for row in plate2.rows():
	plate_a.append(row)

plate_b = []
for row in elute_plate.rows():
	plate_b.append(row)

#for a 96 well plate, 20ul Sample Reaction Volume
#addition of AMPure XP -> total volume in each well = 56ul
m200.transfer(36, source_plate('A1'), plate_a, mix_after=(10,40), new_tip='always', trash=True)

#separate beads for 2min, leave behind 5~6ul supernatant
mag_deck.engage()
m200.delay(120)
m200.transfer(50, plate_a, trash2, new_tip='always', trash=True)

#for 2 times, wash with 200ul ethanol, incubate for 30s, take out ethanol and throw.
#can't use for loop, robot prints 'run out of tips'
#for i in range(2):
m200.transfer(200, source_plate('A3'), plate_a, new_tips='always', trash=True).delay(30)
m200.transfer(200, plate_a, trash2, new_tips='always', trash=True).delay(60)
mag_deck.disengage()

#addition of 40ul elution buffer
m200.transfer(40, source_plate('A5'), plate_a, mix_after=(10, 35), new_tip='always', trash=True)
m200.delay(120)

#separate magnetic beads from mixture
mag_deck.engage()
m200.delay(60)
m200.transfer(5, plate_a, plate_b, new_tip='always', trash=True)
