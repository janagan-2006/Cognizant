# from abc import ABC, abstractmethod
# class Payment(ABC):
#     def __init__(self):
#         print("Payment Constructor")
#     @abstractmethod
#     def pay(self):
#         print("Base Validation")


# class UPI(Payment):

#     def pay(self):
#         super().pay()
#         print("UPI Payment")

# u = UPI()
# u.pay()

# #----------------------

# # Composition
# # Composition = HAS-A Relationship

# # Example:

# class Engine:

#     def start(self):
#         print("Engine Started")
# class Car:

#     def __init__(self):
#         self.engine = Engine()
        
# c = Car()
# c.engine.start()  # Output: Engine Started

# # Question:

# # Does Car have an Engine?

# # Yes.

# # So:

# # Car HAS-A Engine

# # duck typeing is a normal run time polymorphism in python. It is a concept of dynamic typing. In duck typing, the type or class of an object is less important than the methods it defines. If an object behaves like a duck (i.e., it has a quack method), then it can be treated as a duck, regardless of its actual class.
# # class Animal:

# #     def speak(self):
# #         pass
# # class Dog(Animal):

# #     def speak(self):
# #         print("Bark")
# # class Cat(Animal):

# #     def speak(self):
# #         print("Meow")

# # Function:

# # def make_sound(animal):
# #     animal.speak()

# # Usage:

# # make_sound(Dog())
# # make_sound(Cat())

# # Output:

# # Bark
# # Meow

# # This is normal runtime polymorphism.

def summa(a, b):
    print("Sum is:", a + b)
    return a + b
c=summa(5, 10)  # Output: Sum is: 15
# print(c)