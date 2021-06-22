class Queue:

    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        self._list.append(value)

    def dequeue(self):
        first_element = self._list[0]
        self._list.remove(first_element)
        return first_element

    def search(self, index):
        if index < 0 or index > len(self._list) - 1:
            raise IndexError()
        else:
            return self._list[index]
