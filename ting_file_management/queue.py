class Queue:
    def __init__(self):
        self.unread_file = list()

    def __len__(self):
        return len(self.unread_file)

    def enqueue(self, value):
        self.unread_file.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.unread_file[0]
        del self.unread_file[0]
        return value

    def search(self, index):
        if self.is_empty():
            return None
        value = self.unread_file[index]
        return value