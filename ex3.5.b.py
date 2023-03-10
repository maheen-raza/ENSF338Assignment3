import time
import random
import matplotlib.pyplot as plt
import heapq

# Inefficient implementation
def insertion_extraction_inefficient(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    res = []
    while heap:
        res.append(heapq.heappop(heap))
    return res

# Efficient implementation
def insertion_extraction_efficient(nums):
    heap = list(nums)
    heapq.heapify(heap)
    res = []
    while heap:
        res.append(heapq.heappop(heap))
    return res

def time_insertion_extraction(nums, function):
    start_time = time.perf_counter()
    function(nums)
    end_time = time.perf_counter()
    return end_time - start_time

nums = [random.randint(-1000, 1000) for _ in range(1000)]
times_inefficient = []
times_efficient = []
for i in range(100):
    times_inefficient.append(time_insertion_extraction(nums, insertion_extraction_inefficient))
    times_efficient.append(time_insertion_extraction(nums, insertion_extraction_efficient))

plt.hist(times_inefficient, bins=20, alpha=0.5, label='Inefficient')
plt.hist(times_efficient, bins=20, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.show()

print('Average time for inefficient implementation:', sum(times_inefficient)/len(times_inefficient))
print('Average time for efficient implementation:', sum(times_efficient)/len(times_efficient))
