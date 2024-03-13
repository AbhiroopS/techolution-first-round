# Problem 2: Library System
# Question:
# Design a simple library system using OOP. Create classes ‘Book’, ‘ Author’, and ‘Library’. The ‘Book’ class should have attributes for book details (title, ISBN, etc.). The ‘Author’ class should have attributes for author details (name, birthdate, etc.). The ‘Library’ class should manage a collection of books and authors, allowing users to borrow and return books.

from Author import Author
from Book import Book
from Library import Library

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