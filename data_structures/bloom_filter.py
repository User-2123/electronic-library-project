class BloomFilter:
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size # Битовый массив (0 или 1)

    def _hashes(self, item):
        # Генерируем несколько хешей для одного элемента
        # В реальности используют murmur3 или подобные, здесь симуляция
        result = []
        base_hash = hash(item)
        for i in range(self.hash_count):
            # Используем смещение, чтобы получить разные индексы
            result.append((base_hash + i * 12345) % self.size)
        return result

    def add(self, item):
        for index in self._hashes(item):
            self.bit_array[index] = 1 # Ставим биты в 1

    def check(self, item):
        for index in self._hashes(item):
            if self.bit_array[index] == 0:
                return False # Если хоть один бит 0, элемента точно нет
        return True # Все биты 1 — элемент возможно есть