# When we want to apply the same function between all items in a list and return one result
# For example, to get the fastest dog from a list of dogs
 
from functools import reduce

numbers = [1,2,3,4,4,5,6]

# I - 1,2 -> max = 2
# II - max, 3 -> max = 3
# III - max, 4 -> max = 4
# IV - max, max -> max = 4
# V - ...
# VI - ...
# param1, param2: return a if a is higher than b otherwise return b
higher = lambda a, b: a if a > b else b

print(reduce(higher, numbers))

# 1,2 -> 2
# 2, 3 -> 3
# 3, 4 -> 4
# 4, 4 -> 4
# 4, 5 -> 5
# 5, 6 -> 6
# 6

nums = [10,20,30,40,50,60,70,80,90,100]

sum_func = lambda num, num2: num + num2
print(sum_func(5,10))

print(reduce(sum_func, nums))

# 10, 20 -> 30
# 30, 30 -> 60
# 60, 40 -> 100
# 100, 50 -> 150
# 150, 60 -> 210
# 210, 70 -> 280
# 280, 80 -> 360
# 360, 90 -> 450
# 450, 100 -> 550
# 550