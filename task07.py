class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author=author
        self.year  = year



book1 = Book("O'tkan kunlar", "Abdulla Qodiriy", 1925)
book2 = Book("Dunyoning ishlari", "O'tkir Hoshimov", 1982)


print(book1.title, book1.author, book1.year)
print(book2.title, book2.author, book2.year)
