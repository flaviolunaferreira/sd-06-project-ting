class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        if value not in self.queue:
            self.queue.append(value)
            return True
        return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def search(self, index):
        if index not in range(len(self.queue)):
            raise IndexError("Index not in range")
        if self.queue[index]:
            return self.queue[index]


# tingQueue = Queue()
# tingQueue.enqueue(42)
# print(tingQueue.queue[0])
# print("***************")
# tingQueue.enqueue(43)
# print(tingQueue.queue[0])
# print(tingQueue.queue[1])
# print("***************")
# tingQueue.enqueue(44)
# print(tingQueue.queue[0])
# print(tingQueue.queue[1])
# print(tingQueue.queue[2])
# print("***************")
# print(tingQueue.dequeue())
# print(tingQueue.search(4))
