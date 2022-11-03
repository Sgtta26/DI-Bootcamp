# MULTIPLE / UNCPECIFIED AMOUNT OF ARGUMENTS

def capitalize_all_words(*info):
    for i in info:
        print(i.capitalize())

# capitalize_all_words('hello', 'bread', 'cheese', 'atm')

def capitalize_multiply(*info):
    for i in info:
        if isinstance(i, str): 
            print(i.capitalize())
        if isinstance(i, int):
            print(i ** 2)
        if isinstance(i, list):
            print("THERE's A LIST")

capitalize_multiply('hello', 4, 5, 'bread', 'cheese', [1,2,3], 'atm')

