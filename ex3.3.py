import sys

list =[]

oldcapacity= sys.getsizeof(list)

for x in range(64):
    list.append(x)

    if sys.getsizeof(list) != oldcapacity:
        currcapacity = sys.getsizeof(list)
        print(f"{oldcapacity} capacity is changed to {currcapacity} bytes after adding {x+1} elements."
        )