import copy


class Employee:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def clone(self):

        return copy.deepcopy(self)
    
emp1 = Employee(
    "Charles",
    23
)

emp2 = emp1.clone()

emp2.name = "John"

print(emp1.name)
print(emp2.name)