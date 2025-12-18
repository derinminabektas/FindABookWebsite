from domain.book import Book
from temporary_data.books import BOOKS, USER_BOOKS

def get_all_books() -> list[Book]:
    return BOOKS

def get_books_by_user_id(user_id: int) -> list[Book]:
    return USER_BOOKS.get(user_id, [])

def get_book_by_title(title):
    for book in get_all_books():
        if book.title == title:
            return book
    return None