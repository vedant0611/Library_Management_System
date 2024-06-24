# book.py
from storage import Storage
from models import Book

class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.books = self.storage.load_books()

    def add_book(self, title, author, isbn, copies=1):
        # Check if ISBN already exists
        if any(book.isbn == isbn for book in self.books):
            print(f"Error: Book with ISBN {isbn} already exists. Cannot add duplicate.")
            return
        
        # Add new book
        new_book = Book(title, author, isbn, copies)
        self.books.append(new_book)
        self.storage.save_books(self.books)
        print("Book added successfully.")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book.to_dict())

    def search_books(self, attribute, value):
       
        found_books = [book for book in self.books if getattr(book, attribute, None) == value]

        if found_books:
            return found_books
        else:
            print(f"No books found where {attribute} is '{value}'")
            return []

    def update_book(self, isbn, title=None, author=None, copies=None):
        book_found = False
        for book in self.books:
            if book.isbn == isbn:
                book_found = True
                if title:
                    book.title = title
                if author:
                    book.author = author
                if copies is not None:
                    book.copies = copies
                self.storage.save_books(self.books)
                print("Book updated successfully.")
                break
        
        if not book_found:
            print("Book not found.")


    def delete_book(self, isbn):
        book_found = False
        updated_books = []
        
        for book in self.books:
            if book.isbn == isbn:
                book_found = True
            else:
                updated_books.append(book)
        
        if book_found:
            self.books = updated_books
            self.storage.save_books(self.books)
            print("Book deleted successfully.")
        else:
            print("Book not found. Deletion failed.")

book_manager = BookManager(Storage())
