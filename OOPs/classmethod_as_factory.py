# class method is used as a factory.
class Book:
    TYPES = ("hardcover", "papercover")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 500)

    @classmethod
    def papercover(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)


print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1000)
print(book) 
# Factory
hard_book = Book.hardcover("Freedom", 500)
paper_book = Book.papercover("Self Growth", 800)
print(hard_book)
print(paper_book)
