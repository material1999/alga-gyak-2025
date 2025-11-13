class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # update existing
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def __repr__(self):
        return str(self.table)

    def __str__(self):
        return "\n".join(str(item) for item in self.table)


# Example
h = HashTableChaining()
h.insert("apple", 5)
h.insert("banana", 7)
h.insert("orange", 11)
h.insert("watermelon", 9)
h.insert("pear", 15)
print(h)