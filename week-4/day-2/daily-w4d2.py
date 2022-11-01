# challenge 1:

number = int(input("Number: "))
length = int(input("Length: "))
result = []
total = 0
for _ in range(length):
    total += number
    result.append(total)
print(result)


# challenge 2:

word = input("Word: ")
result = word[0]
for symbol in word:
    if result[-1] == symbol:
        continue
    result += symbol
print(result)