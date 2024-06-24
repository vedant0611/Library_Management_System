import json
from models import Book, User

class Storage:
    def __init__(self, book_file='books.json', user_file='users.json'):
        """
        Initialize Storage with default file names for books and users.

        Args:
        - book_file (str): File name to store books (default: 'books.json').
        - user_file (str): File name to store users (default: 'users.json').
        """
        self.book_file = book_file
        self.user_file = user_file

    def load_books(self):
        """
        Load books from JSON file.

        Returns:
        - list: List of Book objects loaded from file, or an empty list if file not found.
        """
        try:
            with open(self.book_file, 'r') as f:
                books_data = json.load(f)
            return [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            return []

    def save_books(self, books):
        """
        Save books to JSON file.

        Args:
        - books (list): List of Book objects to save.
        """
        with open(self.book_file, 'w') as f:
            json.dump([book.to_dict() for book in books], f)

    def load_users(self):
        """
        Load users from JSON file.

        Returns:
        - list: List of User objects loaded from file, or an empty list if file not found.
        """
        try:
            with open(self.user_file, 'r') as f:
                users_data = json.load(f)
            return [User.from_dict(data) for data in users_data]
        except FileNotFoundError:
            return []

    def save_users(self, users):
        """
        Save users to JSON file.

        Args:
        - users (list): List of User objects to save.
        """
        with open(self.user_file, 'w') as f:
            json.dump([user.to_dict() for user in users], f)
