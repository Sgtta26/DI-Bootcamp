class Animal:
    total_animals = 0 
    # class attribute - general to all objects

    def __init__(self, name, age):
        # self - reference to the object 
        self.name = name
        self.age = age
        Animal.total_animals += 1

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog('Bon', 1)
dog2 = Dog('Bob', 2)

cat1 = Cat('Mizz', 3)
cat2 = Cat('Bip', 2)

# print(dog1.total_animals)
print(dog1.__dict__)
print(dog2.__dict__)

