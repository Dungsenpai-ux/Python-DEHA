import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        print(self.heap)

# Example usage
min_heap = MinHeap()
min_heap.push(3)
min_heap.push(1)
min_heap.push(5)
min_heap.push(2)
min_heap.display()
print("Min element:", min_heap.pop())
min_heap.display()
