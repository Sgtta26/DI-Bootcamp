# When there's a list and we want to apply a function on each item inside the list -
#  -> we use the map function

numbers = [1,2,3,4,4,5,6]

# for i in range(len(numbers)):
#     numbers[i] *= 10

multpily = lambda n: n * 10
print(multpily(10))

# map with lambda function
print(list(map(lambda n: n * 10, numbers)))

# map with usual function
def multiply2(num):
    return num * 10

print(list(map(multiply2, numbers)))


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
fruit = list(map(lambda fruit: fruit.lower(), fruit))
print(fruit)