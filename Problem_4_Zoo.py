# Problem 4: Zoo Management
# Question:
# Create a zoo management system using OOP. Design classes for ‘Animal’, ‘Zoo’, and specific animal types like ‘Lion’, ‘Elephant’, and ‘Giraffe’. The ‘Animal’ class should have attributes for animal details, and each specific animal type should have a method to make a sound. The ‘Zoo’ class should manage a collection of animals and have a method to make all animals in the zoo make their respective sounds.

class Animal: # Animal Class that cointains name of the Animal along with a method that returns the Sound that Animal makes
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Lion(Animal): # Lion class Inherits Animal Class and uses the make_sound() method to return lion sounds
    def make_sound(self):
        return f"ROAR!"

class Elephant(Animal): # Elephant class Inherits Animal Class and uses the make_sound() method to return Elephant sounds
    def make_sound(self):
        return f"elephant nosie here"

class Giraffe(Animal): # Giraffe class Inherits Animal Class and uses the make_sound() method to return Giraffe sounds
    def make_sound(self):
        return f"giraffe noise here"

class Zoo: # Zoo Class Definition, has a method for adding animals to its animals[] attribute and another method for Displaying all the Animals in the Zoo along with their Sounds
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def display_animals(self):
        print("Animals in the Zoo:")
        for animal in self.animals:
            print(f"{animal.name}: {animal.make_sound()}")

# Making Zoo Object
zoo = Zoo() 

# Making Objects for all the animals in the zoo, passing the animals name as an argument
giraffe = Giraffe("Girafarig") 
lion = Lion("Entei")
elephant = Elephant("Hollyphant")

# Using add_animal method in zoo object to add the animal to its animals[] attribute
zoo.add_animal(giraffe)
zoo.add_animal(lion)
zoo.add_animal(elephant)

# Using display_animals() method to display list of all animals in the Zoo along with their sounds
zoo.display_animals()