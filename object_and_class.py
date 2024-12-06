class Car:
    name = "pyae"
    def __init__(self,a,b,c,d):
        self.color = a
        self.brand = b
        self.price = c
        self.doors = d

    def car(self,food):
        print(f"This is {food}")


obj = Car("white","bmw","1000",4)
obj.car("meet")
print(obj.color)
print(obj.name)