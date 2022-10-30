
#  +
#  - ​
#  *
#  ** ​
#  /
#  //
#  %
# ​
# ​
#  +=
#  -=
#  *=
# /=
# ​
# """int - integer/whole number
#     0, 12, 124
# ​
#     float - floating number/with decimal spaces
#     0.0, 12.4, 124.9888
# """
# ​
# """string (sequence of characters)
#     'abba'
    
#     'abba'.capitalize() >> 'Abba'
#     'abba'.replace('b','x') >> 'axxa'
# ​
#     a_string * 2 >> 'abbaabba'
# ​
#     STRING CONCATENTAION
#     a_string + 'VVV' >> 'abbaVVV'
#     a_string + ' VVV' >> 'abba VVV'
#     a_string + ' ' + 'VVV' >> 'abba VVV'
# ​
#     * A string is Immutable (cannot be changed)
#     a_string[3] = ' ' >> TypeError: 'str' object does not support item assignment
# ​
#     solution -> break down the string and build it up again
#     left = a_string[:4] >> 'abba'
#     right = a_string[4:] >> 'VVV'
#     a_string = left + ' ' + right >> 'abba VVV'
# ​
#     f-string formatting (f + " {variable1} {variable2}")
#     f""
# """
# ​
# """ 
#     The print function 
    
#     print("Some string to print on screen") >> Some string to print on screen
#     print(123) >> 123
#     print(100 + 500)  >> 600   
#     print("I have", 2, "Apples") >> I have 2 Apples [spaces automatically added]
# ​
# """
# ​
# """
#     The input function - takes an input from the user via keybord and returns a string
# ​
#     input("Here you put your input: ")
#     >> Here you put your input: >> BBADFs
#     >> 'BBADFs'
# ​
#     To store the input inside variable
#     name = input('Please state your name: ')
# """
# ​
# """
#     Condition operators - return True or False
# ​
#     ==
#             True == 1 >> True
#     !=  
#             'Apple' != 'Apple' >> False
# ​
#     <= (Smaller or Equal)
#             'a' <= 'b' >> True
#             'b' <= 'b' >> True
#     >= (Higher or Equal)
#              2 >= 2 >> True
#              3 >= 2 >> True
#     < (Smaller)
#             'a' < 'A' >> False
#     > (Higher)
#             'a' > 'A' >> True
    
# """
# ​
# """
# ​
# >>> user_in = '3' 
# >>> user_in = int(user_in)
# >>> type(user_in)
# <class 'int'>
# ​
# """



# exercice exemple :

# Ask the user for a number between 1 and 100
# If the number is a multiple of three, print "Fizz"
# If the number is a multiple of five, print "Buzz".
# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

number = int(input('Your number between 1 and 100: '))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")   
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print("Buzz")



# exercice exemple 2 :

a = 3
b = 1
name = input("Your name: ")

if a == b:
    print("a and b are equal")
    if name != 'Yossi':
        print("You're welcome")
    else:
        print("Hello again")
elif name == 'Yossi' or b == 2:
    print("Whatever")
else:
    print("FINISHED")