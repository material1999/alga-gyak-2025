from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(words)
print(counter)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
