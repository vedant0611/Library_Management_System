import book
import user
import check

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Add User")
    print("7. List Users")
    print("8. Update User")
    print("9. Delete User")
    print("10. Search User")
    print("11. Checkout Book")
    print("12. Checkin Book")
    print("13. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        
        if choice == '1':
            # Add Book
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            copies = input("Enter number of copies: ")
            try:
                copies = int(copies)
                if copies <= 0:
                    raise ValueError("Number of copies must be a positive integer.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
            
            # Check if ISBN already exists -> to ensure uniqueness
            existing_books = book.book_manager.search_books('isbn', isbn)
            if existing_books:
                print(f"Book with ISBN {isbn} already exists. Cannot add.")
            else:
                book.book_manager.add_book(title, author, isbn, copies)
                print("Book added.")

        elif choice == '2':
            # List Books -> returns the list of avaliable books
            books = book.book_manager.books
            if not books:
                print("No books available.")
            else:
                book.book_manager.list_books()

        elif choice == '3':
            # Update Book -> updates the book according to author
            isbn = input("Enter ISBN of the book to update: ")
            existing_books = book.book_manager.search_books('isbn', isbn)
            if not existing_books:
                print(f"Book with ISBN {isbn} not found.")
                continue
            
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            copies = input("Enter new number of copies (leave blank to keep current): ")
            try:
                copies = int(copies) if copies else None
            except ValueError:
                print("Invalid input for copies. Please enter a number.")
                continue
            
            book.book_manager.update_book(isbn, title, author, copies)

        elif choice == '4':
            # Delete Book -> delete the book
            isbn = input("Enter ISBN of the book to delete: ")
            existing_books = book.book_manager.search_books('isbn', isbn)
            if not existing_books:
                print(f"Book with ISBN {isbn} not found.")
                continue
            
            book.book_manager.delete_book(isbn)
            print("Book deleted.")

        elif choice == '5':
            # Search Book
            attribute = input("Enter attribute to search by (title/author/isbn): ")
            if attribute not in ['title', 'author', 'isbn']:
                print("Invalid attribute. Please enter 'title', 'author', or 'isbn'.")
                continue
            
            value = input(f"Enter value for {attribute}: ")
            books = book.book_manager.search_books(attribute, value)
            if not books:
                print("No books found.")
            else:
                for b in books:
                    print(b.to_dict())

        elif choice == '6':
            # Add User -> creates the user keeping in mind unique ID 
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            existing_users = user.user_manager.search_users('user_id', user_id)
            if existing_users:
                print(f"User with ID {user_id} already exists. Cannot add.")
            else:
                user.user_manager.add_user(user_id, name)
                print("User added.")

        elif choice == '7':
            # List Users
            users = user.user_manager.users
            if not users:
                print("No users available.")
            else:
                user.user_manager.list_users()

        elif choice == '8':
            # Update User -> updates user details using id
            user_id = input("Enter user ID of the user to update: ")
            existing_users = user.user_manager.search_users('user_id', user_id)
            if not existing_users:
                print(f"User with ID {user_id} not found.")
                continue
            
            name = input("Enter new name (leave blank to keep current): ")
            user.user_manager.update_user(user_id, name)

        elif choice == '9':
            # Delete User
            user_id = input("Enter user ID of the user to delete: ")
            existing_users = user.user_manager.search_users('user_id', user_id)
            if not existing_users:
                print(f"User with ID {user_id} not found.")
                continue
            
            user.user_manager.delete_user(user_id)
            print("User deleted.")

        elif choice == '10':
            # Search User
            attribute = input("Enter attribute to search by (name/user_id): ")
            if attribute not in ['name', 'user_id']:
                print("Invalid attribute. Please enter 'name' or 'user_id'.")
                continue
            
            value = input(f"Enter value for {attribute}: ")
            users = user.user_manager.search_users(attribute, value)
            if not users:
                print("No users found.")
            else:
                for u in users:
                    print(u.to_dict())

        elif choice == '11':
            # Checkout Book -> means to update the status of the copies of the book per user (decreadse by one)
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            check.checkout_manager.checkout_book(user_id, isbn)

        elif choice == '12':
            #Checkin Book -> means to update the status of the copies of the book per user (increase by one)
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            check.checkout_manager.checkin_book(user_id, isbn)

        elif choice == '13':
            # Exit the program -> no option selected
            print("Exiting.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
