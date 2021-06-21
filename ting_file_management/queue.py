class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        if value not in self._data:
            return self._data.append(value)

    def dequeue(self):
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        raise IndexError
