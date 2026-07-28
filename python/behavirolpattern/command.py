# Encapsulate a request as an object.

class TV:

    def turn_on(self):
        print("TV ON")

class TurnOnCommand:

    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class Remote:

    def press(self, command):
        command.execute()

tv = TV()

command = TurnOnCommand(tv)

remote = Remote()

remote.press(command)