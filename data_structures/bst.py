class BSTNode:
    def __init__(self, key, value):
        self.key = key        # Ключ для сортировки (например, book_id)
        self.value = value    # Сама книга (объект Book)
        self.left = None      # Левый потомок
        self.right = None     # Правый потомок

class BST:
    def __init__(self):
        self.root = None      # Корень дерева

    def insert(self, key, value):
        if not self.root:
            self.root = BSTNode(key, value) # Если дерево пустое, создаем корень
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if key < node.key:    # Если ключ меньше текущего, идем влево
            if node.left is None:
                node.left = BSTNode(key, value) # Нашли место — вставляем
            else:
                self._insert_recursive(node.left, key, value) # Идем глубже
        elif key > node.key:  # Если ключ больше, идем вправо
            if node.right is None:
                node.right = BSTNode(key, value)
            else:
                self._insert_recursive(node.right, key, value)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key: # Нашли или уперлись в тупик
            return node.value if node else None
        if key < node.key:
            return self._search_recursive(node.left, key) # Ищем слева
        return self._search_recursive(node.right, key)    # Ищем справа