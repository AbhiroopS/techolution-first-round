# Problem 4: Zoo Management
# Question:
# Create a zoo management system using OOP. Design classes for ‘Animal’, ‘Zoo’, and specific animal types like ‘Lion’, ‘Elephant’, and ‘Giraffe’. The ‘Animal’ class should have attributes for animal details, and each specific animal type should have a method to make a sound. The ‘Zoo’ class should manage a collection of animals and have a method to make all animals in the zoo make their respective sounds.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return f"ROAR!"

class Elephant(Animal):
    def make_sound(self):
        return f"elephant nosie here"

class Giraffe(Animal):
    def make_sound(self):
        return f"giraffe noise here"

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def display_animals(self):
        print("Animals in the Zoo:")
        for animal in self.animals:
            print(f"{animal.name}: {animal.make_sound()}")

zoo = Zoo()
giraffe = Giraffe("Girafarig")
lion = Lion("Entei")
elephant = Elephant("Hollyphant")

zoo.add_animal(giraffe)
zoo.add_animal(lion)
zoo.add_animal(elephant)

zoo.display_animals()