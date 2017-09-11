from opentrons import containers, robot, instruments

yvonne_plate = containers.create('yvonne_plate', grid=(16,24), spacing=(4.5,4.5), diameter=3.63, depth=7)

trough2 = containers.load('point', 'C3', 'trough2')
plate2 = containers.load('yvonne_plate','C2', 'plate2')

m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200-rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(name="m200", trash_container=trash2, tip_racks=[m200rack2], min_volume = 30, max_volume = 200, axis ="a", channels = 8)

plate_a = []
for row in plate2.rows('6', to='12'):
	plate_a.append(row.wells('A', length=8, step=2))
	plate_a.append(row.wells('B', length=8, step=2))

m200.pick_up_tip(m200rack2.well('A1'))
#m200.aspirate(200, trough)
m200.distribute(25, trough2['A1'], plate_a, trash=False)
m200.drop_tip(trash2)


#for c in robot.commands():
	#print(c)