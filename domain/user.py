from typing import Set

from domain.book import Book


class User:
    def __init__(self, user_id, name, liked_books: Set[Book]):
        self.user_id = user_id
        self.name = name
        self.liked_books = liked_books

    def likes(self, book) -> bool:
        return book in self.liked_books
