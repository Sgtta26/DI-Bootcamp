with open("secrets.txt", mode='r') as file:
    # .readline -> returns one line at a time
    txt= file.read()
    file.seek(0)
    for _ in range(4):
        line = file.readline()


print(line)