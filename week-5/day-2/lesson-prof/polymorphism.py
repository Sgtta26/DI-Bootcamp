class Car:

    def run_engine(self):
        print("The Car Runs engine")     

class Rocket:

    def run_engine(self):
        print("The Rocket Runs engine")

class AC:

    def run_engine(self):
        print("The AC Runs engine")

car1 = Car()
car2 = Car()

rocket1 = Rocket()
ac1 = AC()
ac2 = AC()

items = [car1, rocket1, car2, ac1, ac2]

for item in items:
    item.run_engine()