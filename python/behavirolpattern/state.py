# here variable state decide which class should call

class NoCard:

    def handle(self):
        print("Insert Card")

class HasCard:

    def handle(self):
        print("Enter PIN")

class ATM:

    def __init__(self):
        self.state = NoCard()

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()