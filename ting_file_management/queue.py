class Queue:
    def __init__(self):
        self.unread_files = list()

    def __len__(self):
        return len(self.unread_files)

    def enqueue(self, value):
        self.unread_files.append(value)

    def dequeue(self):
        return self.unread_files.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.unread_files[index]
