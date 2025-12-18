class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0