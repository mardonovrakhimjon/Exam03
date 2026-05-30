class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Salom, mening ismim {self.name}. Yoshim {self.age} da."

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Salom, mening ismim {self.name}. Yoshim {self.age} da. Men {self.grade}-sinfda o'qiyman. "

person1 = Person("Ali", 30)
print(person1.introduce())

student1 = Student("Vali", 15, 9)
print(student1.introduce())