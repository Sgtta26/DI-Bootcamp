class Human:
    number_of_people = 0


    def __init__(self):
        Human.number_of_people += 1

people = [Human() for _ in range(1000)]
print(Human.number_of_people)

