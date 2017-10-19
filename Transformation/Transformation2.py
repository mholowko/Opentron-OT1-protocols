from opentrons import containers, instruments, robot

hot_plate = containers.load('96-PCR-flat', 'C1', 'hot_plate')
media = containers.load('point', 'C3', 'media')
m1000rack2 = containers.load('tiprack-1000ul', 'A2', 'm1000rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m1000 = instruments.Pipette(
	name = "m1000",
	trash_container = trash2,
	tip_racks = [m1000rack2],
	min_volume = 100,
	max_volume = 1000,
	axis = "a",
	channels = 1)

m1000.transfer(950, media('A1'), hot_plate, new_tip=('always'))

robot.run()
