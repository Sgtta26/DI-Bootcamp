class Animal:
    total_animals = 0 
    # class attribute - general to all objects

    def __init__(self, name, age):
        # self - reference to the object 
        self.name = name
        self.age = age
        Animal.total_animals += 1

class Dog(Animal):
    
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

class Cat(Animal):
    pass

dog1 = Dog('Bon', 1, 5)
cat1 = Cat()