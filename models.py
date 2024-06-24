class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'copies': self.copies
        }

    def from_dict(data):
        return Book(data['title'], data['author'], data['isbn'], data.get('copies', 1))

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name
        }

    def from_dict(data):
        return User(data['user_id'], data['name'])
