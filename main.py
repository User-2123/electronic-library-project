from library_system import ElectronicLibrary
from models.book import Book

library = ElectronicLibrary()

# Добавляем книги
print("--- Добавление книг ---")
library.add_book(Book(10, "1984", "George Orwell", 1949, ["dystopia"]))
library.add_book(Book(25, "Brave New World", "Aldous Huxley", 1932, ["dystopia"]))
library.add_book(Book(50, "Fahrenheit 451", "Ray Bradbury", 1953, ["future"]))
library.add_book(Book(5, "The Great Gatsby", "F. Scott Fitzgerald", 1925, ["classic"]))

# 1. Тест Bloom Filter
print("\n--- Быстрая проверка (Bloom Filter) ---")
print(f"Ищем '1984': {library.check_existence_quick('1984')}")
print(f"Ищем 'Harry Potter': {library.check_existence_quick('Harry Potter')}")

# 2. Тест Trie (Автодополнение)
print("\n--- Автодополнение (Trie) ---")
print(library.autocomplete("Brave")) # Должно найти
print(library.autocomplete("Harry")) # Не должно найти

# 3. Тест Heap (Самая старая книга)
print("\n--- Самая старая книга (Heap) ---")
print(library.get_oldest_book_info()) # Должен быть Гэтсби (1925)

# 4. Тест Fenwick Tree (Статистика)
print("\n--- Статистика (Fenwick Tree) ---")
# У нас ID: 5, 10, 25, 50.
# Диапазон 1-30 должен найти 3 книги (ID 5, 10, 25).
print(library.count_books_in_id_range(1, 30))

# 5. Тест Hash Table
print("\n--- Поиск по ID (Hash Table) ---")
print(library.find_book_by_id(50))