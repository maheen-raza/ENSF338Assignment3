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

# define the range of midpoints to try
min_midpoint = max(len(array) // 100, 1)
midrange = range(min_midpoint, len(array), len(array) // 100)

best_midpoints = {}
for i in range(100):  
    for each_number in search_tasks:
        if each_number not in array:
            continue
        g_midrange = 0
        best_time = float('inf')

        for midpoint in midrange:
            start_time = time.perf_counter()
            match = binarysearch(array, each_number, midpoint)
            end_time = time.perf_counter()
            difference_time = end_time - start_time
            if match and difference_time < best_time:
                best_time = difference_time
                g_midrange = midpoint
        best_midpoints[each_number] = g_midrange
for task, midpoint in best_midpoints.items():
    print(f"Task {task}: Best midpoint = {midpoint}, Best time = {best_time}")


x,y=zip(*best_midpoints.items())

plt.scatter(x, y)
plt.title('Best Midpoints for Binary Search')
plt.xlabel('Search Tasks')
plt.ylabel('Best Midpoints')
plt.show()
