from library_system import ElectronicLibrary
from models.book import Book


library = ElectronicLibrary()

library.add_book(Book(1, "1984", "George Orwell", 1949, ["dystopia"]))
library.add_book(Book(2, "Brave New World", "Aldous Huxley", 1932, ["dystopia"]))
library.add_book(Book(3, "Fahrenheit 451", "Ray Bradbury", 1953, ["future"]))

library.show_all_books()

print("\nПоиск книги:")
result = library.find_book_linear("1984")
print(result if result else "Не найдено")


library.show_history()


print("\nПоиск книги по ID (Hash Table):")
book = library.find_book_by_id(2)
print(book if book else "Не найдено")
