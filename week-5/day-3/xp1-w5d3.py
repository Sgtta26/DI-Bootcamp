# #  ex 1:

# number = -5
# absolute_number = abs (number)
# print (absolute_number)
# y = 6
# x = int (y)
# print (x)
# name = input ("What is your name:")
# print(name)

# class Explanation:
#     "abs - convert number to absolute, int-to integer, input-is for users input"
# print(Explanation.__doc__)


# ex 2:

class Currency:

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __iadd__(self, other):
        self.amount = self.__add__(other)
        return self

    def __add__(self, other):
        if type(other) == int:
            return self.amount + other
        if self.currency != other.currency:
            raise TypeError(
                f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
            )
        return self.amount + other.amount

    def main():
        c1 = Currency("dollar", 5)
        c2 = Currency("dollar", 10)
        c3 = Currency("shekel", 1)
        c4 = Currency("shekel", 10)
        print(str(c1))
        print(int(c1))
        print(repr(c1))
        print(c1 + 5)
        print(c1 + c2)
        print(c1)
        c1 += 5
        print(c1)
        c1 += c2
        print(c1)
        c1 + c3
    main()




