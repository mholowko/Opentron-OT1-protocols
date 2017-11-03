from opentrons import containers, instruments, robot

well20 = containers.create('well20', grid=(4, 5), spacing =(16,21), diameter = 10, depth =33)

trough2 = containers.load('well20', 'C1', 'trough')
plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')
m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200-rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(name="m200", trash_container = trash2, tip_racks=[m200rack2], min_volume=30, max_volume = 200, axis = "a", channels = 8)

plate_a=[]
i=0
for col in plate2.cols():
	for i in range(12):
		plate_a.append(col.wells(i, length=1, step=1))
		i += 1

m200.pick_up_tip(m200rack2.well('A1'))
m200.distribute(25, trough2['A5'], plate_a, trash=True)

for c in robot.commands():
	print(c)
