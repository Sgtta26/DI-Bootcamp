class RPG_CHARACTER:
    # Local scope

    # constructor - constructs objects
    def __init__(self, name, level, character_class, vitality, weapon): # self is the refernce to the object 
        self.name = name
        self.level = level
        self.character_class = character_class
        self.vitality = vitality
        self.weapon = weapon


# Global scope 
conan = RPG_CHARACTER(name='Conan', level=1, character_class='Warrior',vitality=200, weapon='Sword') #Creating and object of type RPG_CHARACTER
print(conan.level)

link = RPG_CHARACTER('Link', 4, 'Rogue', 200, 'Sword')
print(link.character_class)