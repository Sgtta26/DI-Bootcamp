with open('some_text.txt', mode='r') as file:
    lines = file.readlines()

print(lines)

for i, line in enumerate(lines):
    # 0, 'This is line 1'
    lines[i] = str(i) + f': {line}'
    #lines[0] = '0' + ': This is line 1'
    
with open('some_text.txt', mode='w') as file:
    file.writelines(lines)