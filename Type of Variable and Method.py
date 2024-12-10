# type of variable
# type of method

# instance variable
# class variable

class Student:
    uni = "taw ma"
    def __init__(self,name,year,age):
        self.name = name
        self.year = year
        self.age = age

    def set_age(self, age):
        self.age = age
        print("successful")

    def set_name(self):
        return self.name 

    @classmethod
    def cls(cls, uni):
        cls.uni = uni



student_one = Student("ppk","first Year",18)
student_two = Student("ppk","first Year",18)


# student_one.set_age("23")
# print(student_one.age)

# name = student_one.set_name()
# print(name)

Student.cls("uni")
print(Student.uni)


