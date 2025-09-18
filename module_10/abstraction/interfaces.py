from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass
class Book(Printable):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def print_info(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
book = Book("Python Book", "Python author")
book.print_info()