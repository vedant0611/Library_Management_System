# Importing all the funtions in this file
# This is the main file from where the depolyment of the flask application takes place

import book
import user
import check

# Menu to select the books and Perform the operations
# It Performs the task of adding , deleting , updating and searching of the books and user


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

# Proceeds with the function if the Option is avaliable else raises up error

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter number of copies: "))
            book.book_manager.add_book(title, author, isbn, copies)
            
        elif choice == '2':
            book.book_manager.list_books()

        elif choice == '3':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to keep current): ") or None
            author = input("Enter new author (leave blank to keep current): ") or None
            copies = input("Enter new number of copies (leave blank to keep current): ")
            copies = int(copies) if copies else None
            book.book_manager.update_book(isbn, title, author, copies)

        elif choice == '4':
            isbn = input("Enter ISBN of the book to delete: ")
            book.book_manager.delete_book(isbn)

        elif choice == '5':
            attribute = input("Enter attribute to search by (title/author/isbn): ")
            value = input(f"Enter value for {attribute}: ")
            books = book.book_manager.search_books(attribute, value)
            for b in books:
                print(b.to_dict())

        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user.user_manager.add_user(user_id, name)

        elif choice == '7':
            user.user_manager.list_users()

        elif choice == '8':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            user.user_manager.update_user(user_id, name)

        elif choice == '9':
            user_id = input("Enter user ID of the user to delete: ")
            user.user_manager.delete_user(user_id)
            print("User deleted.")

        elif choice == '10':
            attribute = input("Enter attribute to search by (name/user_id): ")
            value = input(f"Enter value for {attribute}: ")
            users = user.user_manager.search_users(attribute, value)
            for u in users:
                print(u.to_dict())

        elif choice == '11':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            check.checkout_manager.checkout_book(user_id, isbn)

        elif choice == '12':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            check.checkout_manager.checkin_book(user_id, isbn)

        elif choice == '13':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
