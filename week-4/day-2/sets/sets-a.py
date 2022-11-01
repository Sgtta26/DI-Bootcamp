# Defining Set

a_set = {1,2,3}
a_set = set()

print(type(a_set))

# Sets for removing duplicates

b_set = {2,2,3,3,4,4,5,6,7,8,9,10}

print(b_set)

a_list_w_duplicates = ['Brazil','Germany','UK','US','Somalia','Brazil','Brazil','US','US','US','US','Brazil','Germany','Germany','Germany']

set_without_duplicates = set(a_list_w_duplicates)

a_list_without_duplicates = list(set_without_duplicates)

print(a_list_without_duplicates)