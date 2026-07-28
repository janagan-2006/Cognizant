class Person:

    def __init__(self, name):
        self.name = name
class Student(Person):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name) # Person.__init__(self, name) direct call
        self.subject = subject

s1 = Student("Alice", 20)
t1 = Teacher("Bob", "Math")
print(s1.name)  # Output: Alice
print(s1.age)   # Output: 20
print(t1.name)  # Output: Bob
print(t1.subject)  # Output: Math

#---------------------

class LivingThing:

    def greet(self):
        print("LivingThing")


class Person(LivingThing):

    def greet(self):
        print("Person")
        super().greet()
        print("End of Person greet")

class Student(Person):

    def greet(self):
        print("Student")
        super().greet()
        print("End of Student greet")

s = Student()

s.greet()