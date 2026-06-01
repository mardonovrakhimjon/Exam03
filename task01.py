name = input("Your name: ")
age = input("Your age: ")

f = open("data.txt", "a")
f.write(f"{name} - {age} yosh\n")