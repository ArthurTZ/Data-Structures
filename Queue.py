"""
Python DataStructure QUEUE
"""

from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def empty(self):
        return len(self.queue) == 0    

    def add(self, element):
        self.queue.append(element)
        print(F'Elemente : {element} added to queue')

    def remove(self):
        if not self.empty():
            element = self.queue.popleft()
            print(F'Elemente : {element} removed from queue')
            return element

        else:
            print(f'The queue is empty, nothing to remove')
            return None


    def next_element(self):
        if not self.empty():
            return self.queue[0]
        else:
            print('The queue is empty')

    def size(self):
        return len(self.queue)                    