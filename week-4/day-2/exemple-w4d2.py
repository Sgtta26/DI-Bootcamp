# exercice lesson :

list1 = [5, 10, 15, 20, 25, 50, 20]

idx = list1.index(20)

list1[idx] *= 10

print(list1)



# EXEMPLES:

# 1

import enum


list1 = [5, 10, 15, 20, 25, 50, 20]

idx = list1.index(20)

# list1[idx] *= 10

# print(list1)

# 2

while 20 in list1:
    print("Removing..")
    list1.remove(20)

print(list1)



a_list = [1,2,'a','asdasd',[123, '331',[]]]
    
problematic = []
for item in a_list:
    if isinstance(item, int):
        problematic.append(item)

for prob_item in problematic:
    while prob_item in a_list:
        a_list.remove(prob_item)

print(a_list)
