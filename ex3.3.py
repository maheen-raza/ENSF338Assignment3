import sys

my_list = []

size = sys.getsizeof(my_list)

for i in range(64):
    my_list.append(i)
    new_size = sys.getsizeof(my_list)
    if new_size != size:
        print(f"Capacity changed from {size} byte to {new_size} bytes.")
        size = new_size


print(my_list)