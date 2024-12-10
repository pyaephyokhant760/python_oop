class Person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.__id = id
    def show_id(self):
        print(self.__id)


first_name = Person("bobo",21,221531)
print(first_name.name)
print(first_name.age)
first_name.show_id()