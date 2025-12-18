class MinHeap:
    def __init__(self):
        self.heap = [] # Храним дерево в массиве

    def parent(self, i):
        return (i - 1) // 2 # Формула индекса родителя

    def left_child(self, i):
        return 2 * i + 1    # Формула левого ребенка

    def right_child(self, i):
        return 2 * i + 2    # Формула правого ребенка

    def insert(self, key):
        self.heap.append(key) # Добавляем в конец
        self._heapify_up(len(self.heap) - 1) # "Всплываем" элемент наверх

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop() # Ставим последний элемент в корень
        self._heapify_down(0)          # "Топим" его вниз
        return root

    def _heapify_up(self, i):
        # Пока элемент меньше родителя, меняем их местами
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            p = self.parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def _heapify_down(self, i):
        min_index = i
        l = self.left_child(i)
        r = self.right_child(i)

        # Ищем наименьшего среди родителя и детей
        if l < len(self.heap) and self.heap[l] < self.heap[min_index]:
            min_index = l
        if r < len(self.heap) and self.heap[r] < self.heap[min_index]:
            min_index = r

        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._heapify_down(min_index) # Рекурсивно идем вниз