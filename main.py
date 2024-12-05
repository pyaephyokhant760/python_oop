class Car:
    def __init__(self,a,b,c,d):
        self.color = a
        self.brand = b
        self.price = c
        self.doors = d

obj = Car("white","bmw","1000",4)

print(obj.color)