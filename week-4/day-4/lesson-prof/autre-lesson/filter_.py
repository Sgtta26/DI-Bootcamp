# when we want to remove items from a list of items based on a condition - we use filter

numbers = [1,2,3,4,4,5,6]

# numbers_filtered = []

# for i, num in enumerate(numbers):
#     if num % 2 == 0:
#         continue
#     else:
#         numbers_filtered.append(num)

# print(numbers_filtered)


numbers_filtered = list(filter(lambda num: num % 2 != 0, numbers))
print(numbers_filtered)

func = lambda num: num % 2 != 0
# [1,  2,  3,  4,  4,  5,  6]
# [T,  F,  T,  F,  F,  T,  F]
# [1       3           5]