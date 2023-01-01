class User:
    # pass
    def __init__(self, user_id, username):
        # print("creating new user...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def folllow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "fabio")
user_2 = User("002", "sebastiano")

user_1.folllow(user_2)

print(f"user_1 followers:{user_1.followers} following:{user_1.following}")
print(f"user_2 followers:{user_2.followers} following:{user_2.following}")