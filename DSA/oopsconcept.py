# class Employee(object):

#     company = "Google"
#     def __new__(cls, summa):
#         print("Creating instance of Employee...")
#         instance = super().__new__(cls)
#         return instance
#     def __init__(self, name):
#         self.name = name
      
# e1=Employee("Alice")
# e2=Employee("Bob")
# print(e1 is e2)
# print(e1.name)
# print(Employee.company)
class Employee:

    count = 0

    def __init__(self):
        Employee.count += 1
e1 = Employee()
e2 = Employee()
e3 = Employee()
print()