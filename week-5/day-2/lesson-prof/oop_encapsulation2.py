class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        if isinstance(price, (int, float)):
            if price > 0: # 1000
                self.__max_price = price
            else:
                raise ValueError("Negative number") # price = -1000
        else:
            raise TypeError("Invalid type") # price = 'ADASDAS'

c = Computer()
c.set_max_price(1000)
c.sell()

