from opentrons import containers, instruments, robot

yvonne_plate = containers.create('yvonne_plate', grid=(16, 24), spacing =(4.5,4.5), diameter = 3.63, depth = 7)

trough2 = containers.load('point', 'C3', 'trough')
plate2 = containers.load('yvonne_plate', 'C2', 'plate2')
m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200-rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(name="m200", trash_container = trash2, tip_racks=[m200rack2], min_volume=30, max_volume = 200, axis = "a", channels = 8)

plate_a=[]
for row in plate2.rows('7', to='12'):
    plate_a.append(row.wells('A', length =2, step=2))
    plate_a.append(row.wells('B', length =2, step=2))
	
plate_b=[]
for row in plate2.rows('19', to='24'):
    plate_b.append(row.wells('A', length =2, step=2))
    plate_b.append(row.wells('B', length =2, step=2))

m200.pick_up_tip(m200rack2.well('A1'))
m200.distribute(25, trough2['A1'], plate_a, trash=True)
m200.pick_up_tip(m200rack2.well('A2'))
m200.distribute(25, trough2['A1'], plate_b, trash=True)
