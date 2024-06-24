# check.py
from book import book_manager  # Import book_manager instance from book module
from user import user_manager  # Import user_manager instance from user module

class CheckoutManager:
    def __init__(self, book_manager, user_manager):
        """
        Initialize CheckoutManager with instances of BookManager and UserManager.

        Args:
        - book_manager (BookManager): Instance of BookManager class.
        - user_manager (UserManager): Instance of UserManager class.
        """
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.checkouts = []  # Initialize an empty list to store checkout records

    def checkout_book(self, user_id, isbn):
        """
        Checkout a book for a user.

        Args:
        - user_id (str): ID of the user checking out the book.
        - isbn (str): ISBN of the book to be checked out.
        """
        # Find user by user_id
        user = next((u for u in self.user_manager.users if u.user_id == user_id), None)
        if user is None:
            print("User not found.")
            return

        # Find book by ISBN
        book = next((b for b in self.book_manager.books if b.isbn == isbn), None)
        if book is None:
            print("Book not found.")
            return

        # Check if copies of the book are available
        if book.copies > 0:
            book.copies -= 1  # Decrease available copies of the book
            self.checkouts.append({'user_id': user_id, 'isbn': isbn})  # Record the checkout
            self.book_manager.storage.save_books(self.book_manager.books)  # Save updated books data
            print("Book checked out successfully.")
        else:
            print("No copies available.")

    def checkin_book(self, user_id, isbn):
        """
        Check in a book for a user.

        Args:
        - user_id (str): ID of the user checking in the book.
        - isbn (str): ISBN of the book to be checked in.
        """
        # Find user by user_id
        user = next((u for u in self.user_manager.users if u.user_id == user_id), None)
        if user is None:
            print("User not found.")
            return

        # Find book by ISBN
        book = next((b for b in self.book_manager.books if b.isbn == isbn), None)
        if book is None:
            print("Book not found.")
            return

        book.copies += 1  # Increase available copies of the book
        # Remove the checkout record for the user and book combination
        self.checkouts = [c for c in self.checkouts if not (c['user_id'] == user_id and c['isbn'] == isbn)]
        self.book_manager.storage.save_books(self.book_manager.books)  # Save updated books data
        print("Book checked in successfully.")

    def list_user_books(self, user_id):
        """
        List books checked out by a specific user.

        Args:
        - user_id (str): ID of the user whose checked out books are to be listed.
        """
        # Get list of ISBNs of books checked out by the user
        user_books = [c['isbn'] for c in self.checkouts if c['user_id'] == user_id]
        if not user_books:
            print("No books checked out by this user.")
            return
        
        # Retrieve book details for each ISBN and print them
        books = [book for book in self.book_manager.books if book.isbn in user_books]
        for book in books:
            print(book.to_dict())

# Instantiate a global CheckoutManager object
checkout_manager = CheckoutManager(book_manager, user_manager)
