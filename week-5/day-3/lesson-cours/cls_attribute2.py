class Human:
    number_of_people = 0
    people = {}

    def __init__(self, name):
        self.name = name

        Human.people[name] = self
        Human.number_of_people += 1


if __name__ == '__main__':

    Human('Yossi')
    Human('Lea')
    Human('David')


    yossi = Human.people['Yossi']
    print(yossi.name)