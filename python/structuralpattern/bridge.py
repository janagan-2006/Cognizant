class Red:

    def apply(self):
        print("Red Color")

class Circle:

    def __init__(self, color):

        self.color = color

    def draw(self):

        print("Circle")

        self.color.apply()

circle = Circle(Red())

circle.draw()