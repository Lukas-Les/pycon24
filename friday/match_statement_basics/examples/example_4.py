from dataclasses import dataclass


@dataclass
class Book:
    name: str
    author: str
    publisher: str


@dataclass
class Game:
    name: str
    publisher: str
    platform: str


item = Book("Divine Comedy", "Aligheri", "Penguin")
item = Game("Super Mario Bros", "Nintendo", "NES")


def display_item(item):
    match item:
        case Book(name, author, _):
            print(f"{name} was written by {author}")
        case Game(name, _, platform):
            print(f"{name} was released for {platform}")
