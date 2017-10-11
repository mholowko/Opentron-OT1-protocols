from opentrons import robot, containers, instruments
from opentrons.util import environment

robot.connect(robot.get_serial_ports_list()[0])

environment.refresh()

exec(open('Transformation1.py').read())
exec(open('Transformation2.py').read())
