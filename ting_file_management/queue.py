class Queue:
    def __init__(self):
        self.__length = 0
        self.row = []

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.row.append(value)
        self.__length += 1

    def dequeue(self):
        self.__length -= 1
        return self.row.pop(0)

    def search(self, index):
        if (index >= self.__length or index < 0):
            raise IndexError("DAME DANE DAMEYO DAME NANOYO")
        return self.row[index]

    def get_all(self):
        return self.row
