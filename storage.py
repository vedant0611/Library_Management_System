# storage.py
import json
from models import Book, User

class Storage:
    def __init__(self, book_file='books.json', user_file='users.json'):
        self.book_file = book_file
        self.user_file = user_file

    def load_books(self):
        try:
            with open(self.book_file, 'r') as f:
                books_data = json.load(f)
            return [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            return []

    def save_books(self, books):
        with open(self.book_file, 'w') as f:
            json.dump([book.to_dict() for book in books], f)

    def load_users(self):
        try:
            with open(self.user_file, 'r') as f:
                users_data = json.load(f)
            return [User.from_dict(data) for data in users_data]
        except FileNotFoundError:
            return []

    def save_users(self, users):
        with open(self.user_file, 'w') as f:
            json.dump([user.to_dict() for user in users], f)
