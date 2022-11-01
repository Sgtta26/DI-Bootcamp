# Infinite loop
# while True:
#     print("something")

a = 5
i = 0
while i < a:
    print("Looping")
    i += 1

user_in = ""

while user_in != 'Quit':
    user_in = input("Your input (Quit for exit): ")
    if user_in == 'Yossi':
        print("Break!")
        break
else:
    print("While loop stopped!")
