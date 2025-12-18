class SegmentTree:
    def __init__(self, data, function=sum):
        self.n = len(data)
        self.function = function # Функция агрегации (sum, min, max)
        # Дерево требует размер 4*n для хранения всех узлов
        self.tree = [0] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            # Лист дерева — это элемент массива
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            # Рекурсивно строим левое и правое поддерево
            self._build(data, 2 * node + 1, start, mid)
            self._build(data, 2 * node + 2, mid + 1, end)
            # Значение узла — результат функции от детей
            self.tree[node] = self.function([self.tree[2 * node + 1], self.tree[2 * node + 2]])

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0 # Диапазон не пересекается (для суммы 0, для min - infinity)
        if l <= start and end <= r:
            return self.tree[node] # Диапазон полностью внутри
        
        mid = (start + end) // 2
        p1 = self._query(2 * node + 1, start, mid, l, r)
        p2 = self._query(2 * node + 2, mid + 1, end, l, r)
        return self.function([p1, p2])