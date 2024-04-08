class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def is_available(self):
        return self.is_available

    def return_book(self):
        self.is_available = True











