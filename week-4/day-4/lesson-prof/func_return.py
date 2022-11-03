a_list = [1,2,3,4,5]

def change_list():
    other_list = a_list.copy()
    other_list[0] = 10
    return other_list

b_list = change_list()

print("A list", a_list)
print("B list", b_list)

def a_plus_b():
    return 1 + 2

result = a_plus_b()
print(result)