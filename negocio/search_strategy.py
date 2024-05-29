from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, books, query):
        pass

class TitleSearchStrategy(SearchStrategy):
    def search(self, books, query):
        return [book for book in books if query.lower() in book.title.lower()]

class AuthorSearchStrategy(SearchStrategy):
    def search(self, books, query):
        return [book for book in books if query.lower() in book.author.lower()]
