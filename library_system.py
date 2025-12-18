from data_structures.linked_list import SinglyLinkedList
from data_structures.hash_table_chain import HashTableChaining


class ElectronicLibrary:
    def __init__(self):
        self.books = []  # Dynamic Array
        self.history = SinglyLinkedList()  # Linked List
        self.book_index = HashTableChaining()  # Hash Table

    def add_book(self, book):
        self.books.append(book)
        self.history.append(book)
        self.book_index.insert(book.book_id, book)
        print("Книга добавлена")

    def remove_book(self, book_id):
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                self.books.pop(i)
                self.history.remove(book_id)
                self.book_index.delete(book_id)
                print("Книга удалена")
                return
        print("Книга не найдена")

    def find_book_linear(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_book_by_id(self, book_id):
        return self.book_index.search(book_id)

    def show_all_books(self):
        for book in self.books:
            print(book)

    def show_history(self):
        print("\nИстория добавления книг:")
        self.history.display()

