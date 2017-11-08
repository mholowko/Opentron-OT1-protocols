# for instructions, please refer to TransformationMASTER.py

from opentrons import containers, instruments, robot

well = containers.create('well', grid=(4, 5), spacing =(18,21), diameter = 10, depth = 33)
tube_rack = containers.load('well', 'B2', 'tube_rack')
source_plate = containers.load('96-PCR-flat', 'C2', 'source_plate')
m200rack2 = containers.load('tiprack-200ul', 'A2', 'm200rack2')
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
for col in source_plate.cols():
	for i in range(12):
		plate_a.append(col.wells(i, length=1, step=1))
		i += 1

m200.pick_up_tip(m200rack2.well('A1'))
for i in plate_a:
	m200.transfer(50, tube_rack.wells('A1'), i, mix_after=(4, 40), trash=True)

robot.run()