class Laptop:

    def __init__(self):

        self.cpu = None
        self.ram = None
        self.ssd = None

    def show(self):

        print(
            self.cpu,
            self.ram,
            self.ssd
        )

class LaptopBuilder:

    def __init__(self):

        self.laptop = Laptop()

    def add_cpu(self, cpu):

        self.laptop.cpu = cpu

        return self

    def add_ram(self, ram):

        self.laptop.ram = ram

        return self

    def add_ssd(self, ssd):

        self.laptop.ssd = ssd

        return self

    def build(self):

        return self.laptop
    
laptop = (
    LaptopBuilder()
        .add_cpu("i7")
        .add_ram("16GB")
        .add_ssd("1TB")
        .build()
)

laptop.show()