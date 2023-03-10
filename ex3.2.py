import json
import time
import matplotlib.pyplot as plt
import numpy as np



def binarysearch(array, checknumber, startmid):
    left=0
    right= len(array)-1
    mid = startmid

    while left <= right:
        if array[mid] == checknumber:
            return True

        elif array[mid] < checknumber:
            left = mid +1
        else:
            right = mid -1
        mid = (left+right)//2








with open('ex2data.json') as f:
    array = json.load(f)

with open('ex2tasks.json') as f:
    searchtasks = json.load(f)

midrange = range(len(array)// 100, len(array), len(array)// 100)

# create lists to store task and midpoint data
task_list = []
midpoint_list = []

for each_number in searchtasks:
    goatmidrange = 0
    besttime = float('inf')

    for midpoint in midrange:
        starttime = time.time()
        match = binarysearch(array, each_number, midpoint)
        endtime = time.time()
        differencetime = endtime-starttime
        if match and differencetime < besttime:
            besttime = differencetime
            goatmidrange = midpoint

    # add task and midpoint to lists
    task_list.append(each_number)
    midpoint_list.append(goatmidrange)

# create scatter plot of task vs. midpoint
plt.scatter(task_list, midpoint_list)
plt.xlabel('Task')
plt.ylabel('Midpoint')
plt.title('Chosen Midpoint for Each Task')

# create line plot of all midpoints
x = np.array(list(range(len(searchtasks))))
y = np.array([midrange[i // 100] for i in range(len(searchtasks))])
plt.plot(x, y, color='red')

plt.show()
