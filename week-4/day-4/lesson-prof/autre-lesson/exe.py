people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# less than or equal to 4 letters
filter_names = lambda name: True if len(name) <= 4 else False
names_filtered = list(filter(filter_names, people))

say_hello = lambda name: f"Hello {name}"
names_hello = list(map(say_hello, names_filtered))

for name in names_hello:
    print(name)