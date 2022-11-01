string = input("write 10 characters :")

if len(string) < 10:
    print("string not long enough")
elif len(string) > 10 : 
    print("string too long")
else :
    print("first char:",string[0])
    print("last char:",string[-1])
    temp_str = ''
    for c in string:
        temp_str =+ c
        print(temp_str)
    
#     print(string[0],string[9])

    for i in range(len(string)):
         print(string[:i+1])
