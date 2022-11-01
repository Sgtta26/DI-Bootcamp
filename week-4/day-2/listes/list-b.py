a_list = [1,'a',2,'b',3,4]

# Adding to end of list
a_list.append(5)
print(a_list)

# Finding the index of 3 for inserting
three_idx = a_list.index(3) + 1

a_list.insert(three_idx, 'c')

print(a_list)

b_list = [10, 20, 30]

# Adds a whole list(as one item) to the end
# a_list.append(b_list)

# Extracts all other's list items into the first one
# a_list += b_list
print(a_list)


