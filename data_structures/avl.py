class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Высота узла (нужна для балансировки)

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Правый поворот (когда перевес слева)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        # Поворот
        x.right = y
        y.left = T2
        # Обновляем высоты
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x # Новый корень поддерева

    # Левый поворот (когда перевес справа)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        # Поворот
        y.left = x
        x.right = T2
        # Обновляем высоты
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key, value):
        # 1. Обычная вставка как в BST
        if not root:
            return AVLNode(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        # 2. Обновляем высоту предка
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Получаем баланс
        balance = self.get_balance(root)

        # 4. Если дисбаланс, делаем повороты
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root