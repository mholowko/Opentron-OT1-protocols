#       INSTRUCTIONS
#	
#	1. Place place necessary items according to the map as shown below
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    MATERIALS NEEDED    ******
#
#	1. 200ul tiprack 					X 4
#	2. 96 well plate with primers 		X 4
#	3. ECHO 384 well palte 				X 1
#	4. trash container 					X 1
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#       ******      MAP -- PHYSICAL LAYOUT OF OPENTRONS   ***********
#
#          A               B               C               D                E
#    _______________________________________________________________________________
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   | tiprack-200ul | 96 well plate | 96 well plate | tiprack-200ul |               |  3
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |    Echo       |     trash     |               |
#   | tiprack-200ul | 96 well plate |384 well plate |   container   |               |  2 
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |               | tiprack-200ul | 96 well plate |               |               |  1
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|


from opentrons import containers, instruments, robot

plate384 = containers.create('plate384', grid=(16,24), spacing=(4.5,4.5), diameter=3.8, depth=10.91)

source_plate = containers.load('trough-12row', 'B2', 'source_plate')
primers1 = containers.load('96-PCR-flat', 'B3', 'primers1')
primers2 = containers.load('96-PCR-flat', 'B2', 'primers2')
primers3 = containers.load('96-PCR-flat', 'C1', 'primers3')
primers4 = containers.load('96-PCR-flat', 'C3', 'primers4')
echoplate = containers.load('plate384', 'C2', 'echoplate')
m200rack = containers.load('tiprack-200ul', 'A3', 'm200-rack')
m200rack2 = containers.load('tiprack-200ul', 'A2', 'm200-rack2')
m200rack3 = containers.load('tiprack-200ul', 'B1', 'm200-rack3')
m200rack4 = containers.load('tiprack-200ul', 'D3', 'm200-rack4')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(
	name = "m200",
	trash_container = trash2,
	tip_racks = [m200rack, m200rack2, m200rack3, m200rack4],
	min_volume = 10,
	max_volume = 200,
	axis = "a",
	channels = 8)



plate_a = []
plate_b = []
plate_c = []
plate_d = []

for row in echoplate.rows('1', to='12'):
    plate_a.append(row.wells('A', length =1, step=2).bottom())

for row in echoplate.rows('1', to='12'):
    plate_b.append(row.wells('B', length =1, step=2).bottom())

for row in echoplate.rows('13', to='24'):
    plate_c.append(row.wells('A', length =1, step=2).bottom())

for row in echoplate.rows('13', to='24'):
    plate_d.append(row.wells('B', length =1, step=2).bottom())


for i in range(12):
	m200.transfer(38, primers1.rows(i), plate_a[i], new_tip='always', trash=True)

for i in range(12):
	m200.transfer(38, primers2.rows(i), plate_b[i], new_tip='always', trash=True)

for i in range(12):
	m200.transfer(38, primers3.rows(i), plate_c[i], new_tip='always', trash=True)

for i in range(12):
	m200.transfer(38, primers4.rows(i), plate_d[i], new_tip='always', trash=True)





