from book import book_manager
from user import user_manager

class CheckoutManager:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager

    def checkout_book(self, user_id, isbn):
        user = next((u for u in self.user_manager.users if u.user_id == user_id), None)
        if user is None:
            print("User not found.")
            return

        book = next((b for b in self.book_manager.books if b.isbn == isbn), None)
        if book is None:
            print("Book not found.")
            return

        if book.copies > 0:
            book.copies -= 1
            self.book_manager.storage.save_books(self.book_manager.books)
            print("Book checked out successfully.")
        else:
            print("No copies available.")

    def checkin_book(self, user_id, isbn):
        user = next((u for u in self.user_manager.users if u.user_id == user_id), None)
        if user is None:
            print("User not found.")
            return

        book = next((b for b in self.book_manager.books if b.isbn == isbn), None)
        if book is None:
            print("Book not found.")
            return

        book.copies += 1
        self.book_manager.storage.save_books(self.book_manager.books)
        print("Book checked in successfully.")

# Instantiate a global CheckoutManager object
checkout_manager = CheckoutManager(book_manager, user_manager)
