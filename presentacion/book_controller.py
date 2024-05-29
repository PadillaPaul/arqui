class BookController:
    def __init__(self, service):
        self.service = service

    def add_book(self, book):
        self.service.add_book(book)

    def remove_book(self, book):
        self.service.remove_book(book)

    def search_by_title(self, title):
        return self.service.search_by_title(title)

    def search_by_author(self, author):
        return self.service.search_by_author(author)
