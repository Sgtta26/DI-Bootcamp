# # ex 1:

# from turtle import title


# def display_message():
#     print('we learned a lot')

# display_message()

# # ex 2 :

# def favorite_book(title):
#     print("One of my favorite books is" + title)

# favorite_book('One of my favorite books is Alice in Wonderland')

# # ex 3:

# def describe_city(name_city, country):
#     print('I live in ' + name_city + 'is in ' + country)

# describe_city('Reykjavik', 'Iceland')


# # ex 4:


# from random import *

# def random(number):
#     x = randint(1, 100)
#     print(x)
    
#     if number < 1:
#         print('number is too small')
#     elif number > 100:
#         print('number is too big')
#     elif number == x:
#         print('success')
#     else:
#         print('Looser')
        
# random(12)


# # ex 5:

# def make_shirt(size, text):
#     print('The size of the shirt is ' + size + ' and the text is ' + text)

# def make_shirt(size= 'L', text = 'I love Python'):
#     print(f'The size of the shirt is {size} and the text is {text}')

# make_shirt()

# def make_shirt(size, text = 'I love Python'):
#     print(f'The size of the shirt is {size} and the text is {text}')

# make_shirt("S")

# def make_shirt(size, text ):
#     print(f'The size of the shirt is {size} and the text is {text}')

# make_shirt("M","I love chocolat")


# # ex 6:

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magician_names):
#     for name in magician_names:
#         print(name)

# show_magicians(magician_names)

# def  make_great(magician_names):
#     for name2 in magician_names:
#         print('the Great ' + name2)

# make_great(magician_names)

# ex 7:


from random import *

def get_random_temp():
    x = randint(-10, 40)
    return(x)

get_random_temp()

def main():
    value = get_random_temp()
    print(f"The temperature right now is {value}")
    if value < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif value > 0 and value < 16:
        print('Quite chilly! Don’t forget your coat')
    elif value > 16 and value < 23:
        print('We are in autumns')
    elif value > 24 and value < 32:
        print('Take sunscreen')
    elif value > 33 and value <= 40:
        print('We are in summer !')
main()


# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().