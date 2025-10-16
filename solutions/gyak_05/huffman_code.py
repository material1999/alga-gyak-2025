import heapq

# Step 1: Define frequencies
freq = {
    'A': 3,
    'B': 4,
    'C': 6,
    'D': 17,
    'E': 21,
    'F': 29
}

# Step 2: Create a min-heap with controlled order for tie-breaking
# We sort by (frequency, symbol) to ensure consistent results
heap = [[weight, [symbol, ""]] for symbol, weight in sorted(freq.items(), key=lambda x: (x[1], x[0]))]
heapq.heapify(heap)

print(heap)

# Step 3: Build Huffman tree
while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)

    print(lo, hi)

    # Assign '0' to lo, '1' to hi
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]

    # Merge nodes
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

# Step 4: Extract codes
huffman_codes = sorted(heapq.heappop(heap)[1:], key=lambda x: x[0])

print("Huffman Codes:")
for symbol, code in huffman_codes:
    print(f"{symbol}: {code}")
