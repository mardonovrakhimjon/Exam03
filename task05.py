import json


fayl = "data.json"

f = open('data.json', 'r')
users = json.load(f)

for user in users:
    print(f"Name: {user['name']}, Age: {user['age']}")
