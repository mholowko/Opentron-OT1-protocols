from opentrons import containers, instruments

# ***** Command  Printer*******
#Place this at the top of the protocol
class command_printer:
    def __init__(self):
        import threading
        self.running = True
        self.printer_thread = threading.Thread(target=self.print_commands)
        self.printer_thread.start()

    def print_commands(self):
        from opentrons import robot
        import time
        command_number = 0
        while self.running:
            while len(robot._commands) > command_number:
                print(robot._commands[command_number])
                command_number += 1
            time.sleep(0.1)

    def stop(self):
        self.running = False

# ***** Command  Printer *******


# *** Command Printer ******
#start the command printer here. Put this before the first command in the protocol
printer = command_printer()
# *** Command Printer ******


##### Your Code Here ######

# *** Command Printer ******
#place this at the end of the protocol
printer.stop()
# *** Command Printer ******
