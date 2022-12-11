
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            return "Book already in library"

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.title
            return f"Book with title {title} was not found"
