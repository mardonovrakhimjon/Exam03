class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def save(self):
        file = open("users.txt", "a")
        file.write(f"{self.username}, {self.email}, {self.is_active}\n")
        file.close()

    def deactivate(self):
        self.is_active = False

def fayldan_oqish():
    file = open("users.txt", "r")
    print(file.read())
    file.close()

user1 = User("ali_faol", "ali@mail.com", True)
user2 = User("vali_nofaol", "vali@mail.com", False)

user1.save()
user2.save()

print("Fayldagi ma'lumotlar:")
fayldan_oqish()
