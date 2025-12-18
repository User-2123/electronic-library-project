class UnionFind:
    def __init__(self, size):
        # parent[i] указывает на родителя элемента i. Сначала каждый сам себе родитель.
        self.parent = list(range(size)) 
        # rank[i] — примерная высота дерева (для оптимизации)
        self.rank = [0] * size

    def find(self, i):
        # Ищем корень множества (представителя)
        if self.parent[i] != i:
            # Сжатие путей: переподвешиваем узел сразу к корню
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Объединение по рангу: меньшее дерево вешаем под большее
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Объединение произошло
        return False # Уже были в одном множестве