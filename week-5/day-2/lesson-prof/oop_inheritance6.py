class Respiratory:

    def breathe(self):
        print("The object is breathing")

class Movement:

    def move(self):
        print("The object os moving")


class Animal(Movement, Respiratory):

    def __init__(self, name):
        self.name = name


animal = Animal('Human')
animal.move()
animal.breathe()