from opentrons import robot, containers, instruments
from opentrons.util import environment

robot.connect(robot.get_serial_ports_list()[0])

environment.refresh()

exec(open('ExtractingDNA1.py').read())
exec(open('ExtractingDNA2.py').read())
exec(open('ExtractingDNA3.py').read())
exec(open('ExtractingDNA4.py').read())
exec(open('ExtractingDNA5.py').read())
exec(open('ExtractingDNA6.py').read())
exec(open('ExtractingDNA7.py').read())
exec(open('ExtractingDNA8.py').read())
