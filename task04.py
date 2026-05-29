import json

name = input("Ismingiz: ")
age = int(input("Yoshingiz: "))
yangi_user = {"name": name, "age": age}

fayl = "data.json"

f = open(fayl, "r")
user = json.load(f)
user = []

user.append(yangi_user)

f = open(fayl, "w")
json.dump(user, f, indent=4)
