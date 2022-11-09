secrets_txt = 'This is a text with\nmultiple lines\n...'
# mode 'w' writes/overwrites a new txt file
with open("new_secrets.txt", mode='w') as file:
    file.write(secrets_txt)

lines = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']
with open("some_text.txt", mode='w') as file:
    file.writelines(lines)
