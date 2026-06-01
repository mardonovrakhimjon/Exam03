import json


y_user = {"name": "asad", "age": 12}

f = open("data.json")
users = json.load(f)

users.append(y_user)

f = open("data.json", "w")
json.dump(users, f)