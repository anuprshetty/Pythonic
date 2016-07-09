# Composition means a BookShelf has many Books.

class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book1 = Book("Python 101")
book2 = Book("Microservices")
print(book1)
print(book2)

bookshelf = BookShelf(book1, book2)
print(bookshelf)
