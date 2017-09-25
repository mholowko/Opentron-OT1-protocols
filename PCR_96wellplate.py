from opentrons import robot, containers, instruments

trough2 = containers.load('96-PCR-flat', 'C3', 'trough2')
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
#dntps 38.4ul #
m2.transfer(39, trough2.wells('A1'), trough2.wells('A3'), trash=True)
#polymerase 19.2ul #
m2.transfer(19, trough2.wells('C1'), trough2.wells('A3'), trash=True)
#template 11.52ul #
m2.transfer(12, trough2.wells('E1'), trough2.wells('A3'), trash=True)
#reaction buffer 384ul#
m2.transfer(384, trough2.wells('G1'), trough2.wells('A3'), trash=True)
#water 1440ul#
m2.transfer(900, trough2.wells('B2'), trough2.wells('A3'), trash=True)
m2.transfer(540, trough2.wells('D2'), trough2.wells('A3'), new_tip='never')
m2.mix(8)
m2.drop_tip(trash2)

m2.distribute(20, trough2.wells('A3'), plate2, trash=True)

for c in robot.commands():
	print(c)
