class Employee():

    instanceofthe_class = None

    def __new__(cls,summa):
        if cls.instanceofthe_class is None:
            print("Creating instance of Employee...")
            cls.instanceofthe_class = super().__new__(cls)
        return cls.instanceofthe_class

    def __init__(self, name):
        self.name = name

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1 is e2) # because same memory space
print(e1.name) # because one instance for this entire project so if you change any value by any reference it will create impact