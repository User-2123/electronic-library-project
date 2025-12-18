from models.book import Book


class ElectronicLibrary:
    def __init__(self):
        self.books = []   # Array / Dynamic Array

    def add_book(self, book):
        self.books.append(book)
        print("Книга добавлена")

    def remove_book(self, book_id):
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                self.books.pop(i)
                print("Книга удалена")
                return
        print("Книга не найдена")

    def find_book_linear(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def show_all_books(self):
        if not self.books:
            print("Библиотека пуста")
            return
        for book in self.books:
            print(book)
