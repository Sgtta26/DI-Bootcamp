a_list = []

for num in range(0, 100, 10):
    a_list.append(num)

print(a_list)

# [<what to put> for <variable> in <Sequence>]
b_list = [num for num in range(0,100,10)]
print(b_list)

c_list = [num*2 for num in range(0,100,10)]
print(c_list)

d_list = [(idx, value) for idx, value in enumerate(c_list)]
print(d_list)

e_list = [num for num in range(101) if num % 2 == 0]
# e_list = []
# for num in range(100):
#     if num % 2 == 0:
#         e_list.append(num)
print(e_list)


# Dictionary comprehension
alphabet = 'ABCDEFG'
a_dict = {idx: value for idx, value in enumerate(alphabet)}
print(a_dict)
