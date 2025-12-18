class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        start_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key: # Обновление
                self.values[index] = value
                return
            
            index = (index + 1) % self.size # Линейное пробирование
            if index == start_index:
                raise Exception("Hash Table is full")
        
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash(key)
        start_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            
            index = (index + 1) % self.size
            if index == start_index:
                return None
        return None