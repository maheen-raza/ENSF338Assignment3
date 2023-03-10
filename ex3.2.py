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
        #print(f"For {each_number}, best midpoint is {goatmidrange} with time: {besttime:.10f} seconds")
plt.scatter(task_list, midpoint_list)
plt.xlabel('Task')
plt.ylabel('Midpoint')
plt.title('Chosen Midpoint for Each Task')
plt.show()