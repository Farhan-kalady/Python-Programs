#Create a class Publisher (name). Derive a class Book (title, author) from Publisher. Derive a class Python (price, no_of_pages) from Book. Write a program that displays information about a Python book. Use base class constructor invocation and method overriding.

class Publisher:
    def __init__(self, name):
        self.name = name
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author
class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display_info(self):
        print(f"{self.title} by {self.author}, ${self.price}")
book = Python("O'Reilly", "Learning Python", "Mark Lutz", 64.99, 1648)
book.display_info()