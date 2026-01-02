import pytest

from domain.book import Book
from service.matching_service import recommend_by_tags, score_books
from repo import book_repo


def test_score_books():
    dune = Book("Dune", {"sci-fi", "politics", "desert"})
    foundation = Book("Foundation", {"sci-fi", "empire"})
    neuromancer = Book("Neuromancer", {"sci-fi", "cyberpunk"})
    hobbit = Book("The Hobbit", {"fantasy", "adventure", "journey"})
    snow_crash = Book("Snow Crash", {"cyberpunk", "sci-fi", "virtual-reality"})


    all_books = [dune, foundation, neuromancer, hobbit, snow_crash]
    user_tags = {"cyberpunk", "sci-fi", "virtual-reality"}
    user_books = [
        Book("Snow Crash", {"cyberpunk", "sci-fi", "virtual-reality"})
    ]
    entered_books = [Book("Snow Crash", {"cyberpunk", "sci-fi", "virtual-reality"})]

    scores = score_books(user_tags, eligible_books)

    assert len(scored) == 3
    assert scored[Book("Dune", {"sci-fi", "politics", "desert"})]== 1
    assert scored[Book("Neuromancer", {"sci-fi", "cyberpunk"})] == 2
    assert scored[Book("Foundation", {"sci-fi", "empire"})] == 1