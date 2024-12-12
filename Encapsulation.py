class Person:
    def __init__(self,name,age,id):
        self.__name = name
        self.__age = age
        self.__id = id

    # def greet(self):
    #     print(f"this is {self.__name} i am {self.__age}")

    def get_name(self):
        return self.__name

student = Person("ppk",18,221531)
student_name = student.get_name()
print(student_name)
