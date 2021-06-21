import queue


class Queue:
    def __init__(self):
        self.q = queue.Queue()

    def __len__(self):
        return self.q.qsize()

    def enqueue(self, value):
        self.q.put(value)

    def dequeue(self):
        return self.q.get()

    def search(self, index):
        if (index > -1 and index < self.__len__()):
            result = None
            i = 0
            while (i < self.__len__()):
                value = self.dequeue()
                self.enqueue(value)
                if (i == index):
                    result = value
                i += 1

            return result
        else:
            raise IndexError()

    def find(self, valueToFind):
        index = -1
        i = 0
        while (i < self.__len__()):
            value = self.dequeue()
            self.enqueue(value)
            if (value == valueToFind):
                index = i
            i += 1
        return index
