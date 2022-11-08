class Animal:
    total_animals = 0 
    # class attribute - general to all objects

    def __init__(self):
        # self - reference to the object 
        Animal.total_animals += 1

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog()
dog2 = Dog()

cat1 = Cat()
cat2 = Cat()

print(dog1.total_animals)