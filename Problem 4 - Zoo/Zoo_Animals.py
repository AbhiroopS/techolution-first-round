from Animal import Animal

class Lion(Animal): # Lion class Inherits Animal Class and uses the make_sound() method to return lion sounds
    def make_sound(self):
        return f"ROAR!"

class Elephant(Animal): # Elephant class Inherits Animal Class and uses the make_sound() method to return Elephant sounds
    def make_sound(self):
        return f"elephant nosie here"

class Giraffe(Animal): # Giraffe class Inherits Animal Class and uses the make_sound() method to return Giraffe sounds
    def make_sound(self):
        return f"giraffe noise here"