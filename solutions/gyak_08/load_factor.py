class HashTable:
    def __init__(self, initial_size=4):
        self.size = initial_size
        self.count = 0
        self.table = [[] for _ in range(initial_size)]

    def _hash(self, key):
        return hash(key) % self.size

    def _load_factor(self):
        return self.count / self.size

    def _rehash(self):
        print(f"🔄 Rehashing... old size={self.size}, new size={self.size * 2}")
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        if self._load_factor() > 0.7:
            self._rehash()
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1
        print(f"Inserted '{key}' → Load factor: {self._load_factor():.2f}")

    def __repr__(self):
        return str(self.table)

    def __str__(self):
        return "\n".join(str(item) for item in self.table)


# Example run
h = HashTable()

for item in ["apple", "banana", "orange", "grape", "pear", "melon", "kiwi"]:
    h.insert(item, 1)

print("\nFinal table:")
print(h)
