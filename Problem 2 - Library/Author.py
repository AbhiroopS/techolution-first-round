class Author: # Define a class Author to store author information (name and birthdate)
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    
    def __str__(self):
        return f"Author: {self.name} (Born {self.birthdate})"