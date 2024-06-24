class Book:
    def __init__(self, title, author, isbn, copies=1):
        """Initialize a Book object with title, author, ISBN, and copies."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def to_dict(self):
        """Convert Book object to a dictionary."""
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'copies': self.copies
        }

    @staticmethod
    def from_dict(data):
        """Create a Book object from a dictionary."""
        return Book(data['title'], data['author'], data['isbn'], data.get('copies', 1))

class User:
    def __init__(self, user_id, name):
        """Initialize a User object with user_id and name."""
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        """Convert User object to a dictionary."""
        return {
            'user_id': self.user_id,
            'name': self.name
        }

    @staticmethod
    def from_dict(data):
        """Create a User object from a dictionary."""
        return User(data['user_id'], data['name'])
