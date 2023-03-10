import json


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

for each_number in searchtasks:
    match = binarysearch(array, each_number, (len(array)//2))

    if match:
        print(f"{each_number} is in the array")
    
