# Problem 4: Zoo Management
# Question:
# Create a zoo management system using OOP. Design classes for ‘Animal’, ‘Zoo’, and specific animal types like ‘Lion’, ‘Elephant’, and ‘Giraffe’. The ‘Animal’ class should have attributes for animal details, and each specific animal type should have a method to make a sound. The ‘Zoo’ class should manage a collection of animals and have a method to make all animals in the zoo make their respective sounds.

from Animal import Animal
from Zoo_Animals import Lion, Giraffe, Elephant
from Zoo import Zoo

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