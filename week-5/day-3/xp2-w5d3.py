# #  ex 1: 

# import func

# def func(self,number):

#     self.number = number

# number1 = func(1)
# number2 = func(2)

# print (func)


# # ex 2:

# import random 


# def number():
#     x = random.randint(1, 100)
#     y = int(input('write a number between 1 and 100:'))
#     if x == y:
#         print('winner')
#     else:
#         print('not the same')

# number()


# # ex 3:

# import random 
# import string

# def letter():
#     string.ascii_letters
#     'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     x = random.choice(string.ascii_letters)
#     print(x)

# letter()


# # ex 4:

# from datetime import date

# def dates():
#     today = date.today()
#     print("Today's date:", today)

# dates()


# # ex 5:

# import datetime

# def january():
#     print(f'The 1st of January is in {datetime.datetime(2023, 1, 1)-datetime.datetime.today().replace(microsecond=0)}')

# january()

# # ex 6: 

# from datetime import *

# def bd (bd='26.04.01 17:56:55'):
#     bd_obj = datetime.strptime(bd, '%d.%m.%y %H:%M:%S')
#     today = datetime.now()
#     print(f'You lived: {today - bd_obj}')

# bd()


# # ex 7 :

# from datetime import *

# def today():
#     print(date.today())
#     print(f'The next holiday are in {date(2022, 12, 28)-date.today()}')

# today()


# # ex 8: 

from datetime import *

def how_old_are_you(age, planet = "Earth"):
    hours_second = 31557600

    orbital_period = {
        "Earth" : 1.0,
        "Mercury" :  0.2408467,
        "Venus" : 0.61519726,
        "Mars" : 1.8808158,
        "Jupiter" : 11.862615,
        "Saturn" : 29.447498,
        "Uranus" : 84.016846,
        "Neptune" : 164.79132
    }
    
    k = hours_second * orbital_period[planet]
    return age / k

list_planet = ["Earth", "Mercury", "Venus", "Mars","Jupiter","Saturn", "Uranus","Neptune"]

for i in list_planet:
    print(f'on planet{i} you will be {how_old_are_you(21)}')


# # ex 9:

# from faker import Faker

# faker = Faker()


# users = []

# dict = {}

# def faker_add(amount):
#     for i in range(amount):
#         dict['name'] = faker.name()
#         dict['address'] = faker.address()
#         dict['language_code'] = faker.language_code()
#         users.append(dict)
#     print(users)

   
# faker_add(5)