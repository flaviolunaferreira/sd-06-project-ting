class Queue:
    def __init__(self):
        self.__queue = []
        self.test = "tes"

    def __len__(self):
        return len(self.__queue)

    def enqueue(self, value):
        if value not in self.__queue:
            self.__queue.append(value)

    def dequeue(self):
        dequeued_item = self.__queue.pop(0)
        return dequeued_item

    def search(self, index):
        if index < 0:
            raise IndexError()
        return self.__queue[index]


if __name__ == "__main__":
    my_queue = Queue()
    print(my_queue.search(0))
