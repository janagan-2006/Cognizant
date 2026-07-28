class Coffee:

    def cost(self):
        return 100
    
class MilkDecorator:

    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 20
    
class SugarDecorator:

    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10
    
coffee = Coffee()

coffee = MilkDecorator(coffee)

coffee = SugarDecorator(coffee)

print(coffee.cost())