# book.py
from storage import Storage  # Import Storage class from storage module
from models import Book  # Import Book class from models module

class BookManager:
    def __init__(self, storage):
        """
        Initialize BookManager with storage instance and load books from storage.

        Args:
        - storage (Storage): Instance of Storage class for data persistence.
        """
        self.storage = storage
        self.books = self.storage.load_books()

    def add_book(self, title, author, isbn, copies=1):
        """
        Add a new book to the system.

        Args:
        - title (str): Title of the book.
        - author (str): Author of the book.
        - isbn (str): ISBN of the book (must be unique).
        - copies (int, optional): Number of copies of the book (default is 1).
        """
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
        """List all books currently stored."""
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book.to_dict())

    def search_books(self, attribute, value):
        """
        Search for books based on a specific attribute.

        Args:
        - attribute (str): Attribute to search by (e.g., 'title', 'author', 'isbn').
        - value (str): Value of the attribute to search for.

        Returns:
        - list: List of Book objects matching the search criteria.
        """
        found_books = [book for book in self.books if getattr(book, attribute, None) == value]

        if found_books:
            return found_books
        else:
            print(f"No books found where {attribute} is '{value}'")
            return []

    def update_book(self, isbn, title=None, author=None, copies=None):
        """
        Update book information based on ISBN.

        Args:
        - isbn (str): ISBN of the book to update.
        - title (str, optional): New title to update. If None, only updates existing fields.
        - author (str, optional): New author to update. If None, only updates existing fields.
        - copies (int, optional): New number of copies to update. If None, only updates existing fields.
        """
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
        """
        Delete a book based on ISBN.

        Args:
        - isbn (str): ISBN of the book to delete.
        """
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

# Create an instance of BookManager using a default Storage instance
book_manager = BookManager(Storage())
