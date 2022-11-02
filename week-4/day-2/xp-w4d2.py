# # ex 1:

# from itertools import count
# from random import randrange


# my_fav_numbers = {3, 5, 7, 9}
# my_list = {10, 11}

# my_fav_numbers.update(my_list)

# my_fav_numbers.remove(9)

# # print(my_fav_numbers)

# friend_fav_numbers = {1,2,6}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# print("Union", our_fav_numbers)


# # ex 2:

# # it,s not possible to add more integers to the tuple because:
# # a list with tuple cannot be modify.

# # ex 3:

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.remove("Blueberries")

# basket.append("Kiwi")
# basket.insert(0,"Apples")

# print(basket.count("Apples"))

# basket.clear()
# print(basket)

# # ex 4:

# # An integer is a whole number and a float is a number that has a decimal place.

# # Use numpy.arange()

# num = 1.5
# num_list = [num]
# for i in range(7):
#     num += 0.5
#     num_list.append(num)
# print(num_list)


# # ex 5:


# for i in range(1,21):
#     print(i)

# for i in range(1,21):
#     if (i%2==0):
#         print(i)


# #  ex 6:

# user_in = ""

# while user_in != 'sarah':
#     user_in = input("what your name ?: ")
#     if user_in == 'sarah':
#         break


# #  ex 7:

# string = input("what your favorite fruit(s) separated by space?")

# separated_string = string.split(" ")
# print(separated_string)

# string_2 = input("input name of any fruits :")
# if string_2 in string:
#     print("You chose one of your favorite fruits! Enjoy!")
# else: 
#     print("You chose a new fruit. I hope you enjoy")


# # ex 8:

# toppings = []

# while True:
#     pizza = input("what toppings do you want ? when you finish write quit")
#     if pizza.lower() != "quit":
#         print(f"we will add {pizza} to your pizza")
#         toppings.append(pizza)
#     else:
#         total = 10 + (2.5*len(toppings))
#         print(f"your toppings are {toppings}, and your total is {total}")
#         break


# # ex 9: // marche pas




# string = int(input("what is your age ? "))
# if string < 3:
#     print("you have free ticket")
# elif string >= 3 and string <= 12:
#     print("your ticket is 10$")
# elif string >12:
#     print("your ticket is 15$")


# total = 0
# while True:

#     string = int(input("what is the age of all the people who want a ticket ?"))
#     if string < 3:
#         pass
#     elif string >= 3 and string <= 12:
#         total += 10
#     elif string >12:
#         total += 15
    
#     print(f"your total is{total}")


# # ex 10:


# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# finished_sandwiches = []

# for i in sandwich_orders[0]:
#     sandwich_orders.pop()
#     finished_sandwiches.append(0)



# // 2e facon avec pop
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# finished_sandwiches = []

# while len(sandwich_orders)  != 0:
    
#     finished_sandwich = sandwich_orders.pop(0)
#     finished_sandwiches.append(finished_sandwich)
#     print(f"I have prepared you a {finished_sandwich}")

# print(f"Finished orders:\n{finished_sandwiches}")

# ex 11:

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []

while len(sandwich_orders)  != 0:

    if sandwich_orders [0] == "Pastrami sandwich":
        del sandwich_orders[0]
        continue
    
    finished_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(finished_sandwich)
    print(f"I have prepared you a {finished_sandwich}")

print(f"Finished orders:\n{finished_sandwiches}")







