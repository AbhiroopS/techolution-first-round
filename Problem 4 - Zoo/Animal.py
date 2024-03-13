class Animal: # Animal Class that cointains name of the Animal along with a method that returns the Sound that Animal makes
    def __init__(self, name):
        self.name = name
    
    def make_sound(self): # Abstract Method, needs to be implemented in Child Classes
        pass