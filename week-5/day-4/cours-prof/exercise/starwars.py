from collections import Counter

# Read the file line by line
with open("star_wars.txt", mode='r') as file:
    text = file.read()

# print(text)

# Read only the 5th line of the file
with open("star_wars.txt", mode='r') as file:
    for _ in range(5):
        line = file.readline()
# print(line)

# Read only the 5th first characters of the file
with open("star_wars.txt", mode='r') as file:
    file.readline()
    file.readline()
    file.readline()
    first_chars = file.read(5)

# print(first_chars)
# Read all the file and return it as a list of strings. Then split each word
with open("star_wars.txt", mode='r') as file:
    lines = file.readlines()

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# filtered_list = list(map(lambda s: s.strip('\n'), ))

filtered_list = []
for line in lines:
    # 'Darth\n' -> 'Darth
    filtered_list.append(line.strip('\n'))

# print(filtered_list)

# counter = {'Darth': 0, 'Lea': 0, 'Luke': 0, 'Yossi'}

# for line in filtered_list:
#     # line = 'Darth'
#     counter[line] += 1

# print(counter)

counter = Counter(filtered_list)
print(counter)

lines.insert(0, 'Yossi\n')

with open('star_wars.txt', mode='w') as file:
    file.writelines(lines)

# Append your first name at the end of the file
with open('star_wars.txt', mode='a') as file:
    file.write('Yossi')


# Append "SkyWalker" next to each first name "Luke"
for idx, line in enumerate(lines):
    if 'Luke' in line:
        lines[idx] = lines[idx].strip('\n') # 'Luke\n' -> 'Luke' 
        lines[idx] += ' SkyWalker\n' # 'Luke Skywalker\n'

with open('star_wars.txt', mode='w') as file:
    file.writelines(lines)