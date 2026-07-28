class A:

    def show(self):
        print("A")

    def call(self):
        self.__show()

    def __show(self):
        print("Private A")


class B(A):

    def __show(self):
        print("Private B")


b = B()

b.call()

# ------------------------------------------
class Parent:

    def __init__(self):
        self.__data = "Parent Data"

    def show(self):
        print(self.__data)


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.__data = "Child Data"


c = Child()

c.show()

print(c.__dict__)