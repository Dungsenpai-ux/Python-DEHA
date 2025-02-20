import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

# Example usage
arr = [5, 3, 8, 1, 2, 7]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)