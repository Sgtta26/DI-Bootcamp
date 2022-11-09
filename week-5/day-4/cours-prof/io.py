with open("secrets.txt", mode='r') as file:
    # .read -> string of all of the text inside file
    txt = file.read()
    
with open("secrets.txt", mode='r') as file:
    # .readlines -> string of all of the text inside file
    txt_lines = file.readlines()

with open("secrets.txt", mode='r') as file:
    # .readline -> returns one line at a time
    txt_line = file.readline()


