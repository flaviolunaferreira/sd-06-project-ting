from collections import deque


class Queue:
    def __init__(self):
        self.fila = deque()

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        self.fila.append(value)

    def dequeue(self):
        return self.fila.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.fila[index]

    def return_data(self):
        return self.fila
