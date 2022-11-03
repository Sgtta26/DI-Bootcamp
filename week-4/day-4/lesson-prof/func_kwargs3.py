def any_args(*args, **kwargs):
    for i in args:
        print(i.capitalize())

    if 'data' in kwargs:
        print("DATA INSIDE!")
    else:
        print("NO DATA INSIDE!")


any_args('hello', 'bread', 'cheese', 'atm', name='Yossi', last_name='Eik', city='TLV', data='213')


# ORDER IN PASSING ARGUMENTS/KEY-VALUE ARGUMENTS TO A FUNCTION
#                   (args, kwargs)
#                (1,2,3, name='Yossi')