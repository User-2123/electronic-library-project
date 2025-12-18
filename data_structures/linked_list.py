class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Храним хвост для быстрого добавления (O(1))

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, key):
        """
        Удаляет узел. Если data - это объект Book, сравнивает по book_id.
        Иначе сравнивает по значению.
        """
        current = self.head
        prev = None

        while current:
            # Проверка: это Книга или просто значение?
            is_match = False
            if hasattr(current.data, 'book_id'):
                if current.data.book_id == key:
                    is_match = True
            elif current.data == key:
                is_match = True

            if is_match:
                if prev:
                    prev.next = current.next
                    if current == self.tail: # Если удаляем хвост
                        self.tail = prev
                else:
                    self.head = current.next # Удаляем голову
                    if not self.head:
                        self.tail = None
                return True # Удалено успешно
            
            prev = current
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next