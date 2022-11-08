class BankAccount:

    def __init__(self, holder):
        self.__holder = holder

    def show_holder(self):
        print(self.__holder)

account1 = BankAccount('Yossi')

account1.show_holder()


