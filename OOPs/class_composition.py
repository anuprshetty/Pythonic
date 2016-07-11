# Composition means a BookShelf has many Books.

from typing import List # List, Tuple, Set etc.


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books
    
    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


book1 = Book("Python 101")
book2 = Book("Microservices")
print(book1)
print(book2)

bookshelf = BookShelf([book1, book2])
print(bookshelf)
