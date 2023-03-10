import random
import timeit
import matplotlib.pyplot as plt

# Generate a sorted array of 10000 elements
arr = [random.randint(0, 10000) for i in range(10000)]
arr.sort()

# Define functions for the two search algorithms
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        elif arr[i] > x:
            return -1
    return -1

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Run the experiment
num_measurements = 100
linear_search_times = []
binary_search_times = []
for i in range(num_measurements):
    x = random.randint(0, 10000)
    linear_search_times.append(timeit.timeit(lambda: linear_search(arr, x), number=1000))
    binary_search_times.append(timeit.timeit(lambda: binary_search(arr, x), number=1000))

# Plot the distribution of measured values
plt.hist(linear_search_times, alpha=0.5, label='Linear Search')
plt.hist(binary_search_times, alpha=0.5, label='Binary Search')
plt.xlabel('Execution Time (Seconds)')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

# Print the aggregate of measured values
print('Linear Search:', 'min:', min(linear_search_times), 'avg:', sum(linear_search_times)/num_measurements)
print('Binary Search:', 'min:', min(binary_search_times), 'avg:', sum(binary_search_times)/num_measurements)
