# class method is used as a factory.
class Book:
    TYPES = ("hardcover", "papercover")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    # If return type of a method is same as the method's class type, then you have to enclose it with double quotes. i.e., "Book"
    # Because at this time, class definition is still in progress. So Python don't recognise the current class. So Python provided this work around.
    @classmethod
    def hardcover(cls, name: str, weight: int) -> "Book":
        return cls(name, cls.TYPES[0], weight + 500)

    @classmethod
    def papercover(cls, name: str, weight: int) -> "Book":
        return cls(name, cls.TYPES[1], weight)


print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1000)
print(book) 
# Factory
hard_book = Book.hardcover("Freedom", 500)
paper_book = Book.papercover("Self Growth", 800)
print(hard_book)
print(paper_book)
