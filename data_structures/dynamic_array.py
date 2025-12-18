import ctypes

class DynamicArray:
    """
    Массив, который увеличивается в 2 раза при переполнении.
    """
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if not 0 <= index < self.count:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def append(self, item):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        
        self.array[self.count] = item
        self.count += 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()