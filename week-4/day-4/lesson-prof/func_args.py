names = ['Bob', 'Yossi', 'Ayala']

def print_name(name):
    print(f"Hello {name}")

for name in names:
    print_name(name)

def add_smth(a, b):
    return a + b

# Passing arguments into function parameters
# with specifying parameter names
result = add_smth(a = 5, b = 10)
# without specufying parameter names
result = add_smth(5, 10)

print(result)

# Return multiple values
def return_two_vals():
    return 4, 5, 6, 7, 8

a, b, c, d, e = return_two_vals()
print(a)
print(b)
print(c)
print(d)
print(e)