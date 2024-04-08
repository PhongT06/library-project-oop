class User:
    def __init__(self, name, library_id, borrowed_books=None):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def get_name(self):
        return self.name

    def get_library_id(self):
        return self.library_id

    def get_borrowed_books(self):
        return self.borrowed_books

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)












