#Transfer 384-well PCR reactions into 4 96-well PCR plates (Microamp) for Qiaxcel

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
#   | tiprack-200ul | 96 well plate | 96 well plate |               |               |  3
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |     trash     |               |
#   | tiprack-200ul |384 well plate | 96 well plate |   container   |               |  2 
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   | tiprack-200ul | tiprack-200ul | 96 well plate |               |               |  1
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|


from opentrons import containers, instruments, robot

plate384 = containers.create('plate384', grid=(16,24), spacing=(4.5,4.5), diameter=3.8, depth=10.91)

source_plate = containers.load('trough-12row', 'B2', 'source_plate')
pcr1 = containers.load('96-PCR-flat', 'B3', 'pcr1')
pcr2 = containers.load('96-PCR-flat', 'C3', 'pcr2')
pcr3 = containers.load('96-PCR-flat', 'C2', 'pcr3')
pcr4 = containers.load('96-PCR-flat', 'C1', 'pcr4')
wellplate = containers.load('plate384', 'B2', 'wellplate')
m200rack = containers.load('tiprack-200ul', 'A3', 'm200-rack')
m200rack2 = containers.load('tiprack-200ul', 'A2', 'm200-rack2')
m200rack3 = containers.load('tiprack-200ul', 'A1', 'm200-rack3')
m200rack4 = containers.load('tiprack-200ul', 'B1', 'm200-rack4')
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

for row in wellplate.rows('1', to='12'):
    plate_a.append(row.wells('A', length =1, step=2).bottom())

for row in wellplate.rows('1', to='12'):
    plate_b.append(row.wells('B', length =1, step=2).bottom())

for row in wellplate.rows('13', to='24'):
    plate_c.append(row.wells('A', length =1, step=2).bottom())

for row in wellplate.rows('13', to='24'):
    plate_d.append(row.wells('B', length =1, step=2).bottom())


for i in range(12):
	m200.transfer(38, plate_a[i], pcr1.rows(i), new_tip='always', trash=True)

for i in range(12):
	m200.transfer(38, plate_b[i], pcr2.rows(i), new_tip='always', trash=True)

for i in range(12):
	m200.transfer(38, plate_c[i], pcr3.rows(i), new_tip='always', trash=True)

for i in range(12):
	m200.transfer(38, plate_d[i], pcr4.rows(i), new_tip='always', trash=True)


