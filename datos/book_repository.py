class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
            self.books.remove(book)

    def find_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]
