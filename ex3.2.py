import json
import time
import matplotlib.pyplot as plt

def binarysearch(array, checknumber, startmid):
    left = 0
    right = len(array) - 1
    mid = startmid

    while left <= right:
        if array[mid] == checknumber:
            return True
        elif array[mid] < checknumber:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return False

with open('ex2data.json') as f:
    array = json.load(f)

with open('ex2tasks.json') as f:
    search_tasks = json.load(f)

midrange = range(len(array) // 50, len(array), len(array) // 50)

best_midpoints = {}
for each_number in search_tasks:
    goat_midrange = 0
    best_time = float('inf')

    for midpoint in midrange:
        start_time = time.perf_counter()
        match = binarysearch(array, each_number, midpoint)
        end_time = time.perf_counter()
        difference_time = end_time - start_time
        if match and difference_time < best_time:
            best_time = difference_time
            goat_midrange = midpoint
    best_midpoints[each_number] = goat_midrange
    print(f"For {each_number}, best midpoint is {goat_midrange} with time: {best_time:.10f} seconds")

x = list(best_midpoints.keys())
y = list(best_midpoints.values())

plt.scatter(x, y)
plt.title('Best Midpoints for Binary Search')
plt.xlabel('Search Tasks')
plt.ylabel('Best Midpoints')
plt.show()
