from opentrons import robot, containers, instruments

tube_rack = containers.load('tube-rack-2ml', 'C3', 'tube_rack')
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
m2.transfer(39, tube_rack.wells('A2'), tube_rack.wells('B1'), trash=True)
#polymerase 19.2ul #
m2.transfer(19, tube_rack.wells('B2'), tube_rack.wells('B1'), trash=True)
#reaction buffer 384ul#
m2.transfer(384, tube_rack.wells('C2'), tube_rack.wells('B1'), trash=True)
#water 1440ul#
m2.transfer(1440, tube_rack.wells('D2'), tube_rack.wells('B1'), new_tip='never')
m2.mix(8)
m2.drop_tip(trash2)

m2.distribute(20, tube_rack.wells('B1'), plate2, trash=True)

for c in robot.commands():
	print(c)
