class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def display_name(self):
        print(f"Name: {self._name} , Age: {self._age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self._employee_id = employee_id

    def display_info(self):
        super().display_name
        print(f"this is {self._employee_id}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, deperment):
        super().__init__(name, age, employee_id)
        self._deperment = deperment

    def display_info(self):
        super().display_info()
        print(f"deperment: {self._deperment}")

employee = Employee("pp",32,33)
employee.display_info()


manager = Manager("Pyae",3,3443,3400)
manager.display_info()

# result = isinstance(p, Person)
# print(result);
