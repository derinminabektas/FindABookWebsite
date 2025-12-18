from typing import Set

class Book:
    def __init__(self, title: str, tags: Set[str]):
        self.title = title
        self.tags = set(tags)

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

    def __hash__(self):
        return hash(self.title)