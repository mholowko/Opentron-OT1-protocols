#       INSTRUCTIONS
#	
#	1. Place place necessary items according to the map as shown below
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    MATERIALS NEEDED    ******
#
#	1. 200ul tiprack 					X 1
#	2. 12-row trough 					X 1
#	3. 384 well palte 					x 1
#	4. trash container 					X 1
#	5. PCR master mix containing template
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#		******    12-ROW TROUGH    *******
#	 __________________________
#	|                          | 12
#	|--------------------------|
#	|                          | 11
#	|--------------------------|
#	|                          | 10
#	|--------------------------|
#	|                          |  9
#	|--------------------------|
#	|                          |  8
#	|--------------------------|
#	|                          |  7
#	|--------------------------|
#	|                          |  6
#	|--------------------------|
#	|                          |  5     
#	|--------------------------|
#	|                          |  4
#	|--------------------------|
#	|                          |  3  
#	|--------------------------|
#	|                          |  2
#	|--------------------------|
#	|PCR master mix(w template)|  1     Add this before starting protocol 
#	 --------------------------
#
#       ******      MAP -- PHYSICAL LAYOUT OF OPENTRONS   ***********
#
#          A               B               C               D                E
#    _______________________________________________________________________________
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |               |               |               |               |               |  3
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |     trash     |               |
#   | tiprack-200ul | 12-row trough |384 well plate |   container   |               |  2 
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |               |               |               |               |               |  1
#   |               |               |               |               |               |
#   |               |               |               |               |               |
#   |_______________________________________________________________________________|

from opentrons import containers, instruments, robot

mastermix = containers.create('mastermix', grid=(16, 24), spacing =(4.5,4.5), diameter = 3.63, depth = 7)

trough2 = containers.load('trough-12row', 'B2', 'trough2')
plate2 = containers.load('mastermix', 'C2', 'plate2')
m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200rack2')
trash2 = containers.load('point', 'D2', 'trash2')

m200 = instruments.Pipette(name="m200", trash_container = trash2, tip_racks=[m200rack2], min_volume=30, max_volume = 200, axis = "a", channels = 8)

plate_a=[]
for row in plate2.rows():
    plate_a.append(row.wells('A', length =2, step=2))
    plate_a.append(row.wells('B', length =2, step=2))

plate_b=[]
for row in plate2.rows('19', to='24'):
    plate_b.append(row.wells('A', length =2, step=2))
    plate_b.append(row.wells('B', length =2, step=2))

m200.pick_up_tip(m200rack2.well('A1'))
m200.distribute(25, trough2['A1'], plate_a, trash=True)



