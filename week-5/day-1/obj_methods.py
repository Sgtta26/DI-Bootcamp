class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self, speed):
        print(f"The car {self.name} is now driving, at speed {speed}")
        print(self)

car1 = Car('Toyota', 'Red')
car2 = Car('Mazda', 'Blue')

car1.drive()
# car1.speed = 200
# print(car1.speed)
# print(car2.speed)
# Global scope
## car1.color 
# Local scope
## self.color