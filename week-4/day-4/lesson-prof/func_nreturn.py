def print_smthng() -> None:
    print("SMTHING")

# for _ in range(100):
#     print_smthng()

a = print_smthng()
print(a)

def welcome():
    message = """
    Welcome to our hotel
    We hope it's gonna be ok"""
    print(message)

welcome()

a_list = [1,2,3,4,5]

def change_list():
    a_list[0] = 10

change_list()
print(a_list)