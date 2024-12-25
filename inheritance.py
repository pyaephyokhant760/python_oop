class FirstClass:
    data = "web"
    def set_data(self,data):
        self.data = data
    
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def test(self):
        print("Testing . . . ")


class ThirdClass(SecondClass):
    def display(self):
        print(f"this is {self.data}")
        

first = FirstClass()
# first.set_data("Kyaw Kyaw")
# first.display()
# print(FirstClass.data)
# print(first.data)
# print(SecondClass.data)

second = SecondClass()
# second.set_data("pyae phyo")
# second.display()
# second.test()

third = ThirdClass()
third.set_data("ppk")
third.display()