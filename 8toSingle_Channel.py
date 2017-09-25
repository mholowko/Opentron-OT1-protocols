from opentrons import containers, instruments, robot

yvonne_plate = containers.create('yvonne_plate', grid=(16, 24), spacing =(4.5,4.5), diameter = 3.63, depth = 7)

trough2 = containers.load('point', 'C3', 'trough')
plate2 = containers.load('yvonne_plate', 'C2', 'plate2')
m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200-rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(name="m200", trash_container = trash2, tip_racks=[m200rack2], min_volume=30, max_volume = 200, axis = "a", channels = 8)

plate_a=[]
for col in plate2.cols():
    plate_a.append(col.wells('1', length=1, step=1))

plate_b=[]
for col in plate2.cols():
    plate_b.append(col.wells('3', length=1, step=1))

m200.pick_up_tip(m200rack2.well('A1'))
m200.distribute(25, trough2['A1'], plate_a, trash=True)
m200.pick_up_tip(m200rack2.well('A2'))
m200.distribute(25, trough2['A1'], plate_b, trash=True)

for c in robot.commands():
	print(c)
  
