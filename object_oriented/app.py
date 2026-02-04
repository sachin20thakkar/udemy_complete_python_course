class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying.")


student_sachin = Student("Sachin", 21)
print(student_sachin.name)  # Output: Sachin
print(student_sachin.age)   # Output: 21
student_sachin.study()      # Output: Sachin is studying.   

student_rahul = Student("Rahul", 22)
print(student_rahul.name)   # Output: Rahul
print(student_rahul.age)    # Output: 22
student_rahul.study()       # Output: Rahul is studying.

Student.study(student_sachin)              # Output: <bound method Student.study of <__main__.Student object at 0x000001D4B2C4D5B0>>