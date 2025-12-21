from repo.book_repo import get_all_books, get_books_by_user_id, get_book_by_title
from domain.book import Book


def collect_user_tags(user_books: list[Book]) -> set[str]:
    user_tags = set()
    for book in user_books:
        user_tags.update(book.tags)
    return user_tags


def score_books(user_tags: set[str], books: list[Book]) -> dict[Book, int]:
    scores = {}
    for book in books:
        score = len(user_tags & book.tags)
        if score > 0:
            scores[book] = score
    return scores


def rank(scored_books: dict[Book, int], limit: int) -> list[str]:
    ranked = sorted(
        scored_books.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return [book.title for book, _ in ranked[:limit]]


def get_eligible_books(user_books, entered_books):
    eligible_books = [
        b for b in get_all_books()
        if b not in user_books and b not in entered_books
    ]
    return eligible_books

def recommend_by_tags(user_id: int, entered_book_titles: list[str]) -> list[str]:
    user_books = get_books_by_user_id(user_id)
    entered_books = titles_to_books(entered_book_titles)
    eligible_books = get_eligible_books(user_books, entered_books)

    user_tags = collect_user_tags(entered_books)
    scores = score_books(user_tags, eligible_books)
    return rank(scores, 6)


def titles_to_books(book_titles: list[str]) -> list[Book]:
    books = []
    for title in book_titles:
        book = get_book_by_title(title)
        if book is not None:
            books.append(book)
    return books
