words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Using dict directly
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1

print(count)  # {'apple': 3, 'banana': 2, 'orange': 1}
