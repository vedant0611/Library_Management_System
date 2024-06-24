# user.py
from storage import Storage
from models import User

class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, user_id, name):
        new_user = User(user_id, name)
        self.users.append(new_user)
        self.storage.save_users(self.users)

    def list_users(self):
        for user in self.users:
            print(user.to_dict())

    def search_users(self, attribute, value):
        return [user for user in self.users if getattr(user, attribute, None) == value]

    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.storage.save_users(self.users)
                return
        print("User not found.")

    def delete_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
        self.storage.save_users(self.users)

user_manager = UserManager(Storage())
