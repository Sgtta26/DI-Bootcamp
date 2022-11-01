from collections import namedtuple


a_tuple = (1,2,3,4)
a_tuple = 1, 2, 3, 4

print(type(a_tuple))
print(a_tuple)

# Tuples not mutable
# a_tuple[0] = 10

info = 'Yossi', 'Eik', '+972567343422', 'Tel Aviv'
print(type(info))

# namedtuple
Info = namedtuple('Info', 'first_name last_name phone address')

some_info = Info('Yossi', 'Eik', '+972567343422', 'Tel Aviv')

print(type(some_info))

print(some_info.first_name)
print(some_info.last_name)