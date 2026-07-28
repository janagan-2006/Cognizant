class Person:

    def introduce(self):
        print("I am a person")
class Student(Person):

    def introduce(self):
        print("I am a student")
class Teacher(Person):

    def introduce(self):
        print("I am a teacher")

people = [
    Student(),
    Teacher()
]

for p in people:
    p.introduce()