class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        start = index
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
            if index == start:
                raise Exception("HashTable is full!")
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        start = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start:
                break
        return None

    def __repr__(self):
        return str(self.table)

    def __str__(self):
        return "\n".join(str(item) for item in self.table)


# Example
h = HashTableLinearProbing()
h.insert("apple", 5)
h.insert("banana", 7)
h.insert("orange", 11)
h.insert("watermelon", 9)
h.insert("pear", 15)
print(h)
