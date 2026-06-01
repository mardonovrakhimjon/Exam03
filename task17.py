class User:
    def __init__(self, username, email, is_active=True):
        self.username = username
        self.email = email
        self.is_active= is_active

    def deactivate(self):
        self.is_active = False
        
    def save(self):
        f = open("users.txt", "a")
        qator = f"{self.username}, {self.email}, {self.is_active}\n"
        f.write(qator)

user1 = User("ali", "ali@mail.com", True)
user1.save()
user2 = User("alisa", "alia@mail.com")
user2.deactivate()
user2.save()
