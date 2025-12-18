class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1) # Индексация с 1

    def update(self, i, delta):
        i += 1  # Переход к 1-based индексации
        while i < len(self.tree):
            self.tree[i] += delta
            # i & (-i) дает последний установленный бит. 
            # Добавляем его, чтобы подняться к следующему диапазону.
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            # Вычитаем последний бит, чтобы спуститься вниз по дереву
            i -= i & (-i)
        return s

    def range_query(self, l, r):
        # Сумма на отрезке [l, r] = Сумма(0...r) - Сумма(0...l-1)
        return self.query(r) - self.query(l - 1)