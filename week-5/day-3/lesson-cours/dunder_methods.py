class Number:

    def __init__(self, val):
        self.val = val

    def __str__(self): # dunder method. dunder - double underscores
        return str(self.val)

    def __gt__(self, other):
        return self.val > other.val

number1 = Number(val = 5)
number2 = Number(val = 3)

num_str = str(number1)

print(number1 < number2)
