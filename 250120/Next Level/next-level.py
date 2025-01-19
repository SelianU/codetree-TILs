user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!

class User:
    def __init__(self, user_id="codetree", user_level="10"):
        self.user_id = user_id
        self.user_level = user_level
    def set_id(self, user_id):
        self.user_id = user_id
    def set_level(self, user_level):
        self.user_level = user_level
    def print(self):
        print(f"user {self.user_id} lv {self.user_level}")

user = User()

user.print()

user.set_id(user2_id)
user.set_level(user2_level)

user.print()