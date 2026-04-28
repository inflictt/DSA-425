# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
import heapq
arr = [2, 4, 1, 3, 5]
# heapify frist then sort it
max_heap = [-x for x in arr]
heapq.heapify(max_heap)
sorted_arr = []
while max_heap:
    sorted_arr.append(-heapq.heappop(max_heap))

sorted_arr.reverse()
print(sorted_arr)
