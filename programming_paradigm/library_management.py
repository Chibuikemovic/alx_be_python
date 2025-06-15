class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
        
class Library:
    def __init__(self):
        self._books = []
        pass
        
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, book):
        """Check out a book from the library."""
        if book in self.books and not book.is_checked_out:
            book.is_checked_out = True
            return True
        return False
    
    def return_book(self, book):
        """Return a checked-out book to the library."""
        if book in self.books and book.is_checked_out:
            book.is_checked_out = False
            return True
        return False
    
    def list_books(self):
        """List all books in the library."""
        return [(book.title, book.author, book.is_checked_out) for book in self.books]
        