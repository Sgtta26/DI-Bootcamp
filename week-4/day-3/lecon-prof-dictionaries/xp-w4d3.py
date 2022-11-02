# # ex 1:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# keys_dictionary = dict(zip(keys,values))

# print(keys_dictionary)


# # ex 2:


# family = {
#     "rick": 43, 'beth': 13, 'morty': 5, 'summer': 8
#     }

# total = int()

# for name, age in family.items():
#     if age < 3:
#         total += 0

#     elif age >= 3 and age <= 12:
#         total += 10

#     elif age >12:
#         total += 15


# print(f"your total is {total}")



# ex 3:

from operator import length_hint
from traceback import print_stack


info = {
    "name": "Zara", 
    "creation_date": 1975, 
    "creator_name":[ 
        "Amancio",
        "Ortega",
        "Gaona" ],

    "type_of_clothes":[
        "men",
        "women",
        "children",
        "home"],

    "international_competitors":[
        "Gap",
        "H&M",
        "Benetton" ],

    "number_stores": 7000, 
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US":[
            "pink", 
            "green" ],

    }}


info['number_stores']= 2

# print(info)

# 4. Print a sentence that explains who Zaras clients are ????

info['country_creation'] = 'Spain'

# print('international_competitors' in info)

info['international_competitors'].append ('Desigual')

del info['creation_date']
# print(info)

# 8. Print the last international competitor.
print(info['international_competitors'][-1])

# 9. Print the major clothes colors in the US
print(info['major_color']['US'])

# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(info))


# 11. Print the keys of the dictionary.
for key, value in info.items():
    print(key)

# 12. Create another dictionary called more_on_zara with the following details:

more_on_zara ={
    "creation_date": 1975,
    "number_stores": 10000,
}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand. 
info.update(more_on_zara)
print(info)

# 14. Print the value of the key number_stores. What just happened ?
print (info['number_stores']) 
# we have thes number to the new dictionary = 10000



# ex 4:

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}

for i in users:
    disney_users_A[i] = users.index(i)
print(disney_users_A)

disney_users_B = {}

for i in users:
    disney_users_B[users.index(i)] = i
print(disney_users_B)

# marche pas
disney_users_C = {}

disney_users_C = sorted(disney_users_A.keys()) + sorted(disney_users_A.values())
print(disney_users_C)


# 4.Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.


disney_users_A = {}

for i in users:
    disney_users_A[i] = users.index(i)
print(disney_users_A)

if :
    print()