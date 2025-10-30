#########################
##### Stack (Verem) #####
#########################

stack = []
stack.append('A')
stack.append('B')
stack.append('C')
print(stack.pop())  # C
print(stack)        # ['A', 'B']

#######################
##### Queue (Sor) #####
#######################

from collections import deque

queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print(queue.popleft())  # A
print(queue)            # deque(['B', 'C'])
