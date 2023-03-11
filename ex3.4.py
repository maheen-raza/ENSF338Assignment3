import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            if (self.tail + 1) % self.size == self.head:
                # Queue is full, wait one second and try again
                print('Queue is full, waiting...')
                self.unlock()
                time.sleep(1)
            else:
                if self.head == -1:
                    # First element being added
                    self.head = 0
                self.tail = (self.tail + 1) % self.size
                self.queue[self.tail] = data
                print(f'Enqueued {data} at index {self.tail}')
                self.unlock()
                return

    def dequeue(self):
        while True:
            self.lock()
            if self.head == -1:
                # Queue is empty, wait one second and try again
                print('Queue is empty, waiting...')
                self.unlock()
                time.sleep(1)
            else:
                data = self.queue[self.head]
                if self.head == self.tail:
                    # Last element being removed
                    self.head = self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                print(f'Dequeued {data} from index {self.head}')
                self.unlock()
                return data

def producer():
    while True:
        data = random.randint(1, 10)
        print(f'Producer generated {data}, waiting {data} seconds...')
        time.sleep(data)
        q.enqueue(data)

def consumer():
    while True:
        data = random.randint(1, 10)
        print(f'Consumer waiting {data} seconds...')
        time.sleep(data)
        item = q.dequeue()
        print(f'Consumer dequeued {item}')

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
