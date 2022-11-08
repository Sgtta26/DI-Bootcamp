from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * (self.radius**2)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Circle(radius={self.radius}, test={self.test})"

    def __add__(self, other):
        radius = self.radius + other.radius
        return Circle(radius)

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        return False
        
    def main():
        c1 = Circle(5)
        c2 = Circle(32)
        c3 = Circle(8)
        print(c1)
        print(c1.get_area())
        print(c1 + c2)
        print(c1 > c2)
        print(c1 == c2)
        l = [c1, c2, c3]
        print(l)
        print(sorted(l))
    main()