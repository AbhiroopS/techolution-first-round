class Book: # Define a class Book to store book information (title, author, isbn, borrowed status.
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False # Book initially not borrowed
    
    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nBorrowed: {'Yes' if self.is_borrowed else 'No'}"
