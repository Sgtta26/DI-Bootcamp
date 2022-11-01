# Looping through sequence of numbers 0,1,2,3,..
for i in range(10):
    print(i)

a = 2
for i in range(1, 11):
    print(f"{a} X {i} = ",i*a)

output = "HELLO"
for _ in range(5):
    print(output)


# Looping through items of a collection
a_list = [1,2,'a','asdasd',[123, '331',[]]]
for item in a_list:
    if item == 'a':
        print("Hooray!")
        continue
    print(item)


for item in a_list:
    pass
else:
    print("Loop finished!")


for i in range(10):
    print(f"Iteration : {i}")
    if i > 5:
        print("Break")
        break
else:
    print("Loop finished without break!")


# Looping with step through range
for i in range(1, 100, 10):
    print(i)

a_list = [1,2,'a','asdasd',[123, '331',[]]]
# Looping with step through list
for item in a_list[::2]:
    print(item)

# 1
# a
# [123, '331', []]