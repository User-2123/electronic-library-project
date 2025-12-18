from data_structures.linked_list import SinglyLinkedList
from data_structures.hash_table_chain import HashTableChaining

from data_structures.avl import AVLTree
from data_structures.heap import MinHeap
from data_structures.trie import Trie
from data_structures.bloom_filter import BloomFilter
from data_structures.fenwick_tree import FenwickTree
# UnionFind и SegmentTree можно использовать для аналитики, подключим их тоже
from data_structures.union_find import UnionFind

class ElectronicLibrary:
    def __init__(self):
        # 1. Основное хранилище (Dynamic Array)
        self.books = []
        
        # 2. История операций (Linked List)
        self.history = SinglyLinkedList()
        
        # 3. Быстрый поиск по ID (Hash Table)
        self.book_index = HashTableChaining()
        
        # 4. Поиск по Году (AVL Tree) - сбалансированное дерево
        # Храним корень дерева. Сначала он None.
        self.year_index = AVLTree()
        self.year_root = None 
        
        # 5. Очередь "Самые старые книги" (Min Heap)
        self.oldest_books_heap = MinHeap()
        
        # 6. Автодополнение названий (Trie)
        self.title_trie = Trie()
        
        # 7. Быстрый фильтр "Есть ли книга?" (Bloom Filter)
        # Размер 1000 бит, 3 хеш-функции
        self.existence_filter = BloomFilter(size=1000, hash_count=3)
        
        # 8. Статистика по ID (Fenwick Tree)
        # Допустим, у нас ID книг до 1000. Позволяет быстро узнать, сколько книг в диапазоне ID [1-50].
        self.id_stats = FenwickTree(1000)

        # 9. Группировка книг (Union Find)
        # Допустим, мы хотим объединять книги в кластеры (например, по жанрам вручную)
        # Создадим структуру на 1000 возможных ID
        self.book_clusters = UnionFind(1000)

    def add_book(self, book):
        # 1. Добавляем в список
        self.books.append(book)
        
        # 2. Добавляем в историю
        self.history.append(book)
        
        # 3. Добавляем в хеш-таблицу (по ID)
        self.book_index.insert(book.book_id, book)
        
        # 4. Добавляем в AVL дерево (по Году)
        # ВАЖНО: AVL insert возвращает новый корень, нужно обновлять self.year_root
        self.year_root = self.year_index.insert(self.year_root, book.year, book)
        
        # 5. Добавляем в Кучу (храним кортеж (год, книга), чтобы сортировка шла по году)
        # Python сравнивает кортежи поэлементно.
        self.oldest_books_heap.insert((book.year, book.title))
        
        # 6. Добавляем в Trie (название)
        self.title_trie.insert(book.title)
        
        # 7. Добавляем в Bloom Filter
        self.existence_filter.add(book.title)
        
        # 8. Обновляем дерево Фенвика (увеличиваем счетчик для этого ID на 1)
        if book.book_id < 1000:
            self.id_stats.update(book.book_id, 1)
            
        print(f"Книга '{book.title}' успешно добавлена во все структуры.")

    def remove_book(self, book_id):
        # Удаление сложно для некоторых структур (Bloom Filter, Heap), 
        # поэтому реализуем удаление только из основных.
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                self.books.pop(i)
                self.history.remove(book_id)
                self.book_index.delete(book_id)
                
                # Из Фенвика можно вычесть
                if book_id < 1000:
                    self.id_stats.update(book_id, -1)
                
                print("Книга удалена из основных хранилищ (List, Hash, History).")
                return
        print("Книга не найдена")

    # --- Методы поиска с использованием новых структур ---

    def find_book_by_id(self, book_id):
        """Поиск через Hash Table O(1)"""
        return self.book_index.search(book_id)

    def check_existence_quick(self, title):
        """
        Быстрая проверка через Bloom Filter.
        Если вернет False -> книги ТОЧНО нет.
        Если True -> возможно есть (надо проверять линейным поиском).
        """
        if not self.existence_filter.check(title):
            return "Книги точно нет (Bloom Filter)"
        else:
            # Если фильтр сказал "возможно есть", ищем реально
            found = self.find_book_linear(title)
            return found if found else "Ложное срабатывание фильтра (книги нет)"

    def find_book_linear(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def autocomplete(self, prefix):
        """Использует Trie для проверки, есть ли книги на эту букву"""
        exists = self.title_trie.starts_with(prefix)
        return f"Есть книги, начинающиеся на '{prefix}'" if exists else "Нет таких книг"

    def get_oldest_book_info(self):
        """Смотрит верхушку MinHeap O(1)"""
        if not self.oldest_books_heap.heap:
            return "Библиотека пуста"
        # heap[0] вернет (year, title)
        year, title = self.oldest_books_heap.heap[0]
        return f"Самая старая книга: {title} ({year})"

    def count_books_in_id_range(self, start_id, end_id):
        """Использует Fenwick Tree для подсчета книг в диапазоне ID"""
        if end_id >= 1000: return "Диапазон вне лимитов статистики"
        count = self.id_stats.range_query(start_id, end_id)
        return f"Количество книг с ID от {start_id} до {end_id}: {count}"

    def show_history(self):
        print("\nИстория добавления книг:")
        self.history.display()