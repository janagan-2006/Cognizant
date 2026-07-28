class Student:

    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):

        if marks >= 0:
            self.__marks = marks

    def get_marks(self):
        return self.__marks
    
s1 = Student("John")
s1.set_marks(85)
print(s1.name)  # Output: John
print(s1.get_marks())  # Output: 85

# ----------------------

class Person:

    def __calculate(self):
        print("Person")
class Student(Person):

    def __calculate(self):
        print("Student")

s1=Student()
s1._Student__calculate() # It will throw error because it is private method and it is not accessible outside the class but it is accessible inside the class
# In Python producted and public both are same but the difference is when we create a API then if I use the public as a class name sorry as a class then it will be used by all other users But if you use a protector that is only used by me and my circuit persons so in in future if I need to change the give me a name in public that will be affected by so many people so that is reason for using protected

# -------------------------------------------------

class Property:
    
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        pass
    @price.getter
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price cannot be negative.")
p1=Property(100000)
print(p1.price)  # Output: 100000
p1.price = 150000
print(p1.price)  # Output: 150000  It converts a method into a managed attribute.
# The main purpose of creating the Property is to avoid the getter setter method traditional method

#Store Function in Variable
def greet():
    print("Hello")

x = greet

x()  # Hello

# Functions can be:
# ✓ Stored in variables
# ✓ Passed as arguments
# ✓ Returned from functions

# following is the bad solution
# def login():

#     print("Starting...")
#     print("Login Logic")
#     print("Completed...")
# because we cant do this for signup , forgot password , logout etc so we need to create a decorator function which will be used for all the functions
def decorator(func):

    def wrapper():

        print("Starting...")

        func()

        print("Completed...")

    return wrapper
@decorator
def login():
    print("Login Logic")

@decorator
def signup():
    print("signup Logic")
# login = decorator(login)    instead of this add @decorator then simply use login()
# signup = decorator(signup)
login()
signup()



def decorator(func):
    print("Starting...yes")
    func()
    print("Completed...yes")

@decorator
def login():
    print("Login Logic")

@decorator
def signup():
    print("signup Logic")

login  # because I am not gave any wrapper class so () is not required
signup

