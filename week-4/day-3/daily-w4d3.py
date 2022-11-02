# challlenge 1:

string = input("give me a word:")

user_dictionary = {}

for i in range(len(string)):
    if string[i] not in user_dictionary:
        user_dictionary[string[i]] = [i]
    else:
        user_dictionary[string[i]].append(i)

print(user_dictionary)