import json

def get_animal(id):
    with open('animal.json', 'r') as f:
        info = json.load(f)


    animals = info['animals']

    for animal in animals:
        if animal['id'] == id:
            return animal

    


print(get_animal(id))

def get_family(id):
    with open('animal.json', 'r') as f:
        info = json.load(f)

    families = info['families']

    for family in families:
        if family['id'] == id:
            return family


# we need to loop through list of dictionaries to get a amimal info
# print(animals)




