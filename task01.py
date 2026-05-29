name = input("Ismingiz: ")
age = input("Yoshingiz: ")

with open("data.txt", "a") as f:
    f.write(f"{name} - {age} yosh\n")
