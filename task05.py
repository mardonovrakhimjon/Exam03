import json

f = open("data.json")
users = json.load(f)

for user in users: 
    print(f"Name: {user['name']}, Age: {user['age']}")