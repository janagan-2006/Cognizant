class student:
    school_name="ABC"  # class variable if it is change by any reference it will change for all reference because it is class variable
    def __init__(self,name,dept,roll_no):
        self.__name=name
        self.__dept=dept
        self.__roll_no=roll_no
    def print(self):
        yield self.__name
        yield self.__dept
        yield self.__roll_no
class dept(student):
    def summa(self):
        super().__init__("hi","cse",34) # throw error because 
s1=dept("Charlesj","CSE",12) # It will work because if a child does not contain the constructor automatically hit use the parent constructor
s2=dept("Charlesj","CSE",12)
for s in s1.print():
    print(s)
# print(s1.__name)
print(s1._student__name)
print(s1.__dict__)
print(s1.summa())
print(s1.__dict__)
s1.school_name="XYZ" # Here it doesn't change the class variable value instead of that it is creating the new instance with that name But it is unlike Java
print(s2.school_name)# Defaultly it access class But if I try to change name by using the object create a new instance
print(student.school_name) # If I change the value by using the then definitely change the value of the origin
print(s1.summada)