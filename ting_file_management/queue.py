class Queue:
    def __init__(self):
        self.data = {}
        self.next_in = -1
        self.next_out = -1

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.next_in += 1
        self.data[self.next_in] = value

    def dequeue(self):
        self.next_out += 1
        value_dequeue = self.data[self.next_out]
        del self.data[self.next_out]
        return value_dequeue

    def search(self, index):
        if index in self.data.keys():
            return self.data.get(index)
        else:
            raise IndexError
