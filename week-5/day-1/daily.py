class Farm:

    def __init__(self, farm_name):
      self.farm_name = farm_name
      self.animals = {}
    
    def add_animal(self, name, amount):
        if name not in self.animals:
            self.animals[name] = amount
        else: 
            self.animals[name]+= amount 


    def get_animal_types(self):
        type2 = []
        for animal in self.animals.keys():
            type2.append(animal)
        return type2


    def get_short_info(self):
        info = self.get_animal_types()
        return f'McDonald’s farm has {info}'

mcdo = Farm('mcdo')
mcdo.add_animal('cow',5)
mcdo.add_animal('sheep',2)
mcdo.add_animal('goat',12)

print(mcdo.animals)
print(mcdo.get_animal_types())

print(mcdo.get_short_info())

