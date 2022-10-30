string = input("write 10 characters :")

if len(string) < 10:
    print("string not long enough")
elif len(string) > 10 : 
    print("string too long")

print(string[0],string[9])

for i in range(len(string)):

    print(string[:i+1])
