# Library Management System

This project is a simple Library Management System implemented in Python. It allows users to manage books and users, perform CRUD operations on books and users, and handle book checkouts and check-ins.

## Features

- **Add, List, Update, Delete, and Search Books**
- **Add, List, Update, Delete, and Search Users**
- **Checkout and Checkin Books**
- **Display Books Allocated to Each User**

## Requirements

- Python 3.6

## Project Structure

```plaintext
├── book.py
├── check.py
├── main.py
├── models.py
├── storage.py
└── user.py
```

### Description of Files

- `book.py`: Manages book-related operations.
- `check.py`: Handles the checkout and check-in operations.
- `main.py`: Main entry point for the application.
- `models.py`: Contains the `Book` and `User` model classes.
- `storage.py`: Handles data storage and retrieval using JSON.
- `user.py`: Manages user-related operations.

## Usage

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Run the application:**

   ```sh
   python main.py
   ```

3. **Follow the on-screen menu to perform various operations:**

   - Add Book
   - List Books
   - Update Book
   - Delete Book
   - Search Book
   - Add User
   - List Users
   - Update User
   - Delete User
   - Search User
   - Checkout Book
   - Checkin Book
   - List User Books
   - Exit


## Edge Cases Handled

- Ensure books have unique ISBN numbers.
- Ensure users have unique user IDs.
- Handle cases where books or users are not found.
- Check for available copies before allowing checkout.
- Ensure the book is checked out before allowing check-in.

## Contribution

-Contributions are welcome! Feel free to open issues or submit pull requests.
