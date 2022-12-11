class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content

class FilePrinter:
    def format(self, book:Book):
        with open("text.txt", "a") as writer:
            return writer.write(book.content)


class Printer:
    def __init__(self,formatter):
        self.formatter=formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


book=Book("neshto si")
formatter=FilePrinter()
printer=Printer(formatter)


