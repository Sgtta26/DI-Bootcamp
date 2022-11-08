
# # ex 1:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# all_cats = [Bengal('cat1',2), Chartreux('cat2',5), Siamese('cat3',1)]

# sarah_pets = Pets(all_cats)

# sarah_pets.walk()


# # ex 2:

# class Dog():
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f'{self.name} is barking'

#     def run_speed(self):
#         return f'{self.weight/self.age*10} is the speed of the dog'

#     def fight(self, other_dog):
#         running_speed = self.run_speed()

#         if running_speed * self.weight > other_dog.run_speed() * other_dog.weight:
#             print(f'{self.name} is the winner')
#         else: 
#             print(f'{other_dog.name} is the winner')

# dog1 = Dog('dog1', 1, 11)
# dog2 = Dog('dog2', 2, 22)
# dog3 = Dog('dog3', 3, 33)

# dog1.fight(dog2)
# dog2.fight(dog3)


# ex 3:

import random 
# tjrs doit etre en heut de la page !!!! IMPORTANT

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        return f'{self.weight/self.age*10} is the speed of the dog'

    def fight(self, other_dog):
        running_speed = self.run_speed()

        if running_speed * self.weight > other_dog.running_speed() * other_dog.weight:
            return f'{self.name} is the winner'
        else: 
            return f'{other_dog.name} is the winner'



class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.trained = True
        self.bark ()

    def play(self):
        print(f'{self.name} all play together')

    def do_a_trick(self):
        if self.trained == True:
            x = random.randint(0,3)
            if x == 0:
                print(f'{self.name} does a barrel roll')
            elif x == 1:
                print(f'{self.name} stands on his back legs')
            elif x == 2:
                print(f'{self.name} shakes your hand')
            elif x == 3:
                print(f'{self.name} plays dead')


dog1 = PetDog('dog1', 1, 11)
dog2 = PetDog('dog2', 2, 22)
dog3 = PetDog('dog3', 3, 33)

dog1.train()

dog1.do_a_trick()


