class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def introduce(self):
        return f"Mening ismim {self.name}, yoshim {self.age}da"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade= grade

    def introduce(self):
        return f"Mening ismim {self.name}, yoshim {self.age}da va men {self.grade}-kursman"


inson1 = Person("Anna", 16)
inson2 = Student("Alina", 19, 1)

print(inson1.introduce())
print(inson2.introduce())