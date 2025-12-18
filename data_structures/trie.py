class TrieNode:
    def __init__(self):
        self.children = {} # Словарь: буква -> узел
        self.is_end_of_word = False # Флаг: здесь заканчивается слово?

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() # Создаем ветку, если нет
            node = node.children[char] # Идем глубже
        node.is_end_of_word = True # Помечаем конец слова

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False # Буквы нет — слова нет
            node = node.children[char]
        return node.is_end_of_word # Слово есть, только если это конец

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True # Префикс найден