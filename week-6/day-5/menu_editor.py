from xp1 import *

def load_manager(name, price)->MenuItem:
    return MenuItem(name, price)

load_manager('salad', 40)

def show_user_menu():
    output = """
    (a) Add an item
    (d) Delete an item
    (v) View the menu
    (x) Exit
"""
    print(output)

show_user_menu()

# def add_item_to_menu():
#     name = input ("Name the new item: ")
#     price = int(input(f"Price of {name}: "))

#     item = load_manager(name, price)
#     try: 
#         item.save()
#     except psycopg2.errors.UniqueViolation:
#         print("Can't add duplicate")

# # add_item_to_menu()

def remove_item_from_menu():
    name = input("Item to delete: ")
    item = MenuItem.get_by_name(name)
    if not item:
        print("There is no such item")
    else:
        MenuItem.delete()

def show_restaurant_menu():
    print(MenuItem.all())



remove_item_from_menu()

