###############################
##### Queue with 2 stacks #####
###############################

class QueueUsingStacks:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        """Add an item to the queue (O(1))."""
        self.in_stack.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.out_stack:
            # Move all elements from in_stack to out_stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            print("Queue is empty.")
            return None

        return self.out_stack.pop()

    def peek(self):
        """Return the front item without removing it."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            print("Queue is empty.")
            return None

        return self.out_stack[-1]

    def is_empty(self):
        """Check if the queue is empty."""
        return not (self.in_stack or self.out_stack)

    def __repr__(self):
        # Display the logical order (front → rear)
        if self.out_stack:
            out = self.out_stack[::-1]
        else:
            out = []
        return str(out + self.in_stack)

q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue:", q)   # [10, 20, 30]

print("Dequeue:", q.dequeue())  # 10
print("Queue:", q)   # [20, 30]

q.enqueue(40)
print("Peek:", q.peek())  # 20
print("Dequeue:", q.dequeue())  # 20
print("Queue:", q)   # [30, 40]
