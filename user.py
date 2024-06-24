# user.py
from storage import Storage  # Importing Storage class from storage module
from models import User  # Importing User class from models module

class UserManager:
    def __init__(self, storage):
        """
        Initialize UserManager with storage instance.
        
        Args:
        - storage (Storage): Instance of Storage class for data persistence.
        """
        self.storage = storage
        self.users = self.storage.load_users()  # Load users from storage on initialization

    def add_user(self, user_id, name):
        """
        Add a new user to the system.

        Args:
        - user_id (str): User ID for the new user.
        - name (str): Name of the new user.
        """
        # Check if user with the same user_id already exists
        if any(user.user_id == user_id for user in self.users):
            print(f"User with ID '{user_id}' already exists. Cannot add duplicate users.")
            return
        
        new_user = User(user_id, name)
        self.users.append(new_user)
        self.storage.save_users(self.users)  # Save updated user list to storage
        print("User added successfully.")
        
    def list_users(self):
        """List all users currently stored."""
        for user in self.users:
            print(user.to_dict())

    def search_users(self, attribute, value):
        """
        Search for users based on a specific attribute.

        Args:
        - attribute (str): Attribute to search by (e.g., 'user_id').
        - value (str): Value of the attribute to search for.

        Returns:
        - list: List of User objects matching the search criteria.
        """
        if attribute == 'user_id':
            return [user for user in self.users if user.user_id == value]
        else:
            return []  # Return empty list if attribute is not recognized

    def update_user(self, user_id, name=None):
        """
        Update user information based on user ID.

        Args:
        - user_id (str): User ID of the user to update.
        - name (str, optional): New name to update. If None, only updates existing fields.
        """
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.storage.save_users(self.users)  # Save updated user list to storage
                return
        print("User not found.")  # Print message if user ID is not found in the list

    def delete_user(self, user_id):
        """
        Delete a user based on user ID.

        Args:
        - user_id (str): User ID of the user to delete.
        """
        self.users = [user for user in self.users if user.user_id != user_id]
        self.storage.save_users(self.users)  # Save updated user list to storage

# Create an instance of UserManager using a default Storage instance
user_manager = UserManager(Storage())
