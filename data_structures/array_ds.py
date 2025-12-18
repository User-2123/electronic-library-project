import ctypes

class StaticArray:
    """
    Реализация массива фиксированного размера.
    Имитирует низкоуровневый массив.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        # Создаем массив ссылок фиксированного размера через ctypes
        self.array = (self.capacity * ctypes.py_object)()

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if not 0 <= index < self.count:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def insert(self, index, value):
        if self.count >= self.capacity:
            raise OverflowError("Array is full")
        if not 0 <= index <= self.count:
            raise IndexError("Index out of bounds")
        
        # Сдвигаем элементы вправо
        for i in range(self.count, index, -1):
            self.array[i] = self.array[i - 1]
        
        self.array[index] = value
        self.count += 1

    def delete(self, index):
        if not 0 <= index < self.count:
            raise IndexError("Index out of bounds")
        
        # Сдвигаем элементы влево
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
            
        self.count -= 1