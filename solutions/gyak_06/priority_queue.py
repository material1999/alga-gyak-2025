#######################################
##### Priority Queue / Heap Queue #####
#######################################

import heapq

pq = []
heapq.heappush(pq, (2, "B"))
heapq.heappush(pq, (1, "A"))
heapq.heappush(pq, (3, "C"))

while pq:
    priority, item = heapq.heappop(pq)
    print(priority, item)

# heapq: min-heap

heap = [20, 5, 15, 22, 40]
heapq.heapify(heap)
print(heap)  # [5, 20, 15, 22, 40] (részben rendezett)
heapq.heappush(heap, 3)
print(heapq.heappop(heap))  # 3