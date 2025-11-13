class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """Simple hash function based on Python's built-in hash()"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Naive insert (no collision handling yet)"""
        index = self._hash(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None


# Example
h = HashTable()
h.insert("apple", 10)
print(h.get("apple"))  # Output: 10
