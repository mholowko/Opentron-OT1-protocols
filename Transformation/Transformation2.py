# for instructions, please refer to TransformationMASTER.py

from opentrons import containers, instruments, robot

plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')
media = containers.load('point', 'C3', 'media')
m200rack2 = containers.load('tiprack-200ul', 'B3', 'm1000rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack2],
	min_volume = 300,
	max_volume = 50,
	axis = "a",
	channels = 8)

plate_a=[]
i=0
for col in plate2.cols():
	for i in range(12):
		plate_a.append(col.wells(i, length=1, step=1))
		i += 1

m200.pick_up_tip(m200rack2.well('A1'))
m200.distribute(950, media['A1'], plate_a, trash=True)


robot.run()