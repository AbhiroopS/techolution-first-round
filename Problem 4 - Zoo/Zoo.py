class Zoo: # Zoo Class Definition, has a method for adding animals to its animals[] attribute and another method for Displaying all the Animals in the Zoo along with their Sounds
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def display_animals(self):
        print("Animals in the Zoo:")
        for animal in self.animals:
            print(f"{animal.name}: {animal.make_sound()}")