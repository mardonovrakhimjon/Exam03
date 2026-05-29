class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("O'tkan kunlar", "Abdulla Qodiriy", 1925)
book2 = Book("Dunyoning ishlari", "O'tkir Hoshimov", 1982)

print(f"Kitob 1: {book1.title}, Muallif: {book1.author}, Yili: {book1.year}")
print(f"Kitob 2: {book2.title}, Muallif: {book2.author}, Yili: {book2.year}")