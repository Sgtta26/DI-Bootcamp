# # ex 1:

# from functools import reduce

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat('Jerry', 3)
# cat2 = Cat('Tom', 2)
# cat3 = Cat('Batya', 5)


# cats = [cat1, cat3,cat2]

# # I
# def oldest_cat_func(list_of_cats):
#     oldest_cat = cats[0]

#     for cat in list_of_cats:
#         if oldest_cat.age < cat.age:
#             oldest_cat=cat

#     print(oldest_cat.name)


# # II
# oldest_cat_func = lambda cat1, cat2: cat1 if cat1.age > cat2.age else cat2
# oldest_cat = reduce(oldest_cat_func, cats)

# print(oldest_cat.name)



# # ex 2:

# class Dog:

#     def __init__(self, name: str, height: int):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         x = self.height * 2
#         print(f"{self.name} jumps {x} cm high!")

#     def __str__(self):
#         return f"{self.name}, {self.height}"
        
# davids_dog = Dog('Rex', 50)

# print(davids_dog)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog('Teacup', 20)
# print(sarahs_dog)
# sarahs_dog.bark()
# sarahs_dog.jump()

# bigger_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name

# print(bigger_dog)


# # ex 3:


# class Song:

#     def __init__(self, lyrics):
#         self.lyrics = lyrics


#     def sing_me_a_song(self):
#         for song in self.lyrics:
#             print(song)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()


# ex 4:


class Zoo:

    def __init__(self, zoo_name):
       self.zoo_name = zoo_name
       self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            return(self.animals)

    def get_animals(self):
        print(self.animals)

    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    #  and groups them together based on their first letter. 
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        group_animals = {}
    
    for animal in sort_animals:
        if animal[0] not in group_animals:



ramat_gan_safari = Zoo("sarah")
# animal =  Zoo("dog")
# animal.add_animal()


ramat_gan_safari.add_animal('dog')
ramat_gan_safari.add_animal('snake')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animals('dog')
ramat_gan_safari.get_animals()