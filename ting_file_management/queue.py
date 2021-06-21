from collections import deque


class Queue:
    def __init__(self):
        self.unread_files = deque()

    def __len__(self):
        return len(self.unread_files)

    def enqueue(self, value):
        self.unread_files.append(value)

    def dequeue(self):
        return self.unread_files.pop_front()

    def search(self, index):
        if index < 0:
            return None
        return self.unread_files[index]
