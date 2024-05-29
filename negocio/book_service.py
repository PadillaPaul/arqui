class BookService:
    def __init__(self, repository):
        self.repository = repository

    def add_book(self, book):
        self.repository.add_book(book)

    def remove_book(self, book):
        self.repository.remove_book(book)

    def search_by_title(self, title):
        return self.repository.find_by_title(title)

    def search_by_author(self, author):
        return self.repository.find_by_author(author)
