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