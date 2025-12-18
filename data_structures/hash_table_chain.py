class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        # Создаем список списков (цепочек)
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        
        # Проверяем, есть ли уже такой ключ, чтобы обновить
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Если нет, добавляем
        bucket.append((key, value))

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False