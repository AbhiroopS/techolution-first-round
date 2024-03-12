# Problem 2: Library System
# Question:
# Design a simple library system using OOP. Create classes ‘Book’, ‘ Author’, and ‘Library’. The ‘Book’ class should have attributes for book details (title, ISBN, etc.). The ‘Author’ class should have attributes for author details (name, birthdate, etc.). The ‘Library’ class should manage a collection of books and authors, allowing users to borrow and return books.

class Author: # Define a class Author to store author information (name and birthdate)
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    
    def __str__(self):
        return f"Author: {self.name} (Born {self.birthdate})"

class Book: # Define a class Book to store book information (title, author, isbn, borrowed status.
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False # Book initially not borrowed
    
    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nBorrowed: {'Yes' if self.is_borrowed else 'No'}"

class Library: # Define a class Library to manage a collection of books
    def __init__(self):
        self.books = {} # Dictionary to store books with ISBN as key

    def add_book(self, book):  # Add a book instance to the library collection
        self.books[book.isbn] = book

    def remove_book(self, isbn): # Remove a book from the library collection by ISBN
        if isbn in self.books:
            del self.books[isbn]
            print(f"\nBook with ISBN {isbn} removed from the library")
        else:
            print(f"\nNo Book with ISBN {isbn} found in the library")

    def display_books(self): # Print details of all books in the library
        print('Books available in the library:')
        for isbn, book in self.books.items():
            print(book)
    
    def borrow_book(self, isbn):  # Attempt to borrow a book by ISBN
        if isbn in self.books:
            if not self.books[isbn].is_borrowed:
                self.books[isbn].is_borrowed = True
                print(f"\nBook with ISBN {isbn} borrowed successfully")
            else:
                print(f"\nBook with ISBN {isbn} is already borrowed.")
        else:
            print(f"\nNo book found with ISBN {isbn}.")
    
    def return_book(self, isbn): # Attempt to return a book by ISBN
        if isbn in self.books:
            if self.books[isbn].is_borrowed:
                self.books[isbn].is_borrowed = False
                print(f"\nBook with ISBN {isbn} returned successfully")
            else:
                print(f"\nBook with ISBN {isbn} is not borrowed.")
        else:
            print(f"\nNo book found with ISBN {isbn}.")

# Create a library instance
my_library = Library()

# Create some author instances
author1 = Author("J.R.R. Tolkien", "1892-01-03")
author2 = Author("George R.R. Martin", "1948-09-20")

# Create some book instances
book1 = Book("The Lord of the Rings", author1, "978-0261102694")
book2 = Book("A Song of Ice and Fire", author2, "978-0552140688")

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)

# Display books before borrowing
print("\n**Books in library before borrowing:**")
my_library.display_books()

# Borrow a book
my_library.borrow_book("978-0261102694")  # ISBN for The Lord of the Rings

# Display books after borrowing
print("\n**Books in library after borrowing The Lord of the Rings:**")
my_library.display_books()

# Try to borrow an unavailable book
my_library.borrow_book("978-0261102694")  # ISBN for The Lord of the Rings (already borrowed)

# Return a book
my_library.return_book("978-0552140688")  # ISBN for A Song of Ice and Fire

# Display books after returning
print("\n**Books in library after returning A Song of Ice and Fire:**")
my_library.display_books()