import book
import user
import check

# Function to display the main menu and get user choice
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
    print("13. List User Books")
    print("14. Exit")
    choice = input("Enter choice: ")
    return choice

# Main function to handle user interactions
def main():
    while True:
        choice = main_menu()

        if choice == '1':
            # Add a new book to the library
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter number of copies: "))
            book.book_manager.add_book(title, author, isbn, copies)

        elif choice == '2':
            # List all books in the library
            book.book_manager.list_books()

        elif choice == '3':
            # Update an existing book details
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to keep current): ") or None
            author = input("Enter new author (leave blank to keep current): ") or None
            copies = input("Enter new number of copies (leave blank to keep current): ")
            copies = int(copies) if copies else None
            book.book_manager.update_book(isbn, title, author, copies)

        elif choice == '4':
            # Delete a book from the library
            isbn = input("Enter ISBN of the book to delete: ")
            book.book_manager.delete_book(isbn)

        elif choice == '5':
            # Search for a book in the library
            attribute = input("Enter attribute to search by (title/author/isbn): ")
            value = input(f"Enter value for {attribute}: ")
            books = book.book_manager.search_books(attribute, value)
            if not books:
                print("No books found.")
            for b in books:
                print(b.to_dict())

        elif choice == '6':
            # Add a new user to the system
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user.user_manager.add_user(user_id, name)

        elif choice == '7':
            # List all users in the system
            user.user_manager.list_users()

        elif choice == '8':
            # Update an existing user details
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            user.user_manager.update_user(user_id, name)

        elif choice == '9':
            # Delete a user from the system
            user_id = input("Enter user ID of the user to delete: ")
            user.user_manager.delete_user(user_id)

        elif choice == '10':
            # Search for a user in the system
            attribute = input("Enter attribute to search by (name/user_id): ")
            value = input(f"Enter value for {attribute}: ")
            users = user.user_manager.search_users(attribute, value)
            if not users:
                print("No users found.")
            for u in users:
                print(u.to_dict())

        elif choice == '11':
            # Checkout a book for a user
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            check.checkout_manager.checkout_book(user_id, isbn)

        elif choice == '12':
            # Checkin a book for a user
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            check.checkout_manager.checkin_book(user_id, isbn)

        elif choice == '13':
            # List all books checked out by a user
            user_id = input("Enter user ID: ")
            check.checkout_manager.list_user_books(user_id)

        elif choice == '14':
            # Exit the program
            print("Exiting.")
            break
        else:
            # Handle invalid choices
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
