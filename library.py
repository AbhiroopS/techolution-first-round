# Problem 2: Library System
# Question:
# Design a simple library system using OOP. Create classes ‘Book’, ‘ Author’, and ‘Library’. The ‘Book’ class should have attributes for book details (title, ISBN, etc.). The ‘Author’ class should have attributes for author details (name, birthdate, etc.). The ‘Library’ class should manage a collection of books and authors, allowing users to borrow and return books.

class Author:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    
    def __str__(self):
        return f"Author: {self.name} (Born {self.birthdate})"

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nBorrowed: {'Yes' if self.is_borrowed else 'No'}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed from the library")
        else:
            print(f"No Book with ISBN {isbn} found in the library")

    def display_books(self):
        print('Books available in the library:')
        for isbn, book in self.books.items():
            print(book)
    
    def borrow_book(self, isbn):
        if isbn in self.books:
            if not self.books[isbn].is_borrowed:
                self.books[isbn].is_borrowed = True
                print(f"Book with ISBN {isbn} borrowed successfully")
            else:
                print(f"Book with ISBN {isbn} is already borrowed.")
        else:
            print(f"No book found with ISBN {isbn}.")
    
    def return_book(self, isbn):
        if isbn in self.books:
            if self.books[isbn].is_borrowed:
                self.books[isbn].is_borrowed = False
                print(f"Book with ISBN {isbn} returned successfully")
            else:
                print(f"Book with ISBN {isbn} is not borrowed.")
        else:
            print(f"No book found with ISBN {isbn}.")