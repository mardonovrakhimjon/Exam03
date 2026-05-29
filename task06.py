import json

yangi_user = {"name": "Ali", "age": 15}
fayl = "data.json"

f = open(fayl, "r")
user_list = json.load(f)
f.close()

user_list.append(yangi_user)

f = open(fayl, "w")
json.dump(user_list, f, indent=4)
f.close()

print("Foydalanuvchi JSON faylga qo‘shildi!")
