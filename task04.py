import json

name = input("Ismingiz: ")
age = int(input("Yoshingiz: "))
yangi_user = {"name": name, "age": age}

user = []

f = open("data.json")
user = json.load(f)

user.append(yangi_user)

f = open("data.json", "w")
json.dump(user, f)