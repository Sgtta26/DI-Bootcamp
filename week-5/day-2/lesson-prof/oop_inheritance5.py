class A:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.color}|{self.x}|{self.y}'

class B(A):

    def __init__(self, color, x, y, z):
        super().__init__(color, x, y)
        self.z = z

    def __str__(self):
        old = super().__str__()
        old += f'|{self.z}'
        return old

b = B('Red', 10, 20, 30)
print(b)