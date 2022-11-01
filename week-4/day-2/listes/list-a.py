empty_list = []

# print(type(empty_list))
# print(len(empty_list))

a_list = [1,2,'a','asdasd',[123, '331',[]]]
        #   0 1  2      3       4
a_string = 'Hello, this is Python course'
a_string_list = list(a_string)

# print(a_string_list)
# print(a_string_list.index(' '))

# Indexing
print(a_list[0])
print(a_list[4])
print(a_list[-1])
print(a_list[-2])

print(a_list[0:2])
print(a_list[-3:-1])

print(a_list[0::2])

# [start: end : step]
# [ 0: ALL ITEMS : 1]

print(type(a_list[-1][-1]))

a_list[-1][-1].append(100000000)
print(a_list)
print(a_list[-1][-1][0])