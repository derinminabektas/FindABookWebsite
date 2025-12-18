from domain.book import Book

BOOKS: list[Book] = [
    Book("Dune", {"sci-fi", "politics", "desert"}),
    Book("Neuromancer", {"sci-fi", "cyberpunk"}),
    Book("Foundation", {"sci-fi", "empire"}),
    Book("Brave New World", {"dystopia", "sci-fi"}),
    Book("The Hobbit", {"fantasy", "adventure", "journey"}),
    Book("Fahrenheit 451", {"dystopia", "censorship", "books"}),
    Book("Snow Crash", {"cyberpunk", "sci-fi", "virtual-reality"}),
    Book("The Left Hand of Darkness", {"sci-fi", "sociology", "gender"}),
]

USER_BOOKS: dict[int, list[Book]] = {
    1: [
    ]
}


