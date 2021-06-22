class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queque = list()

    def __len__(self):
        """expor o tamanho da nossa fila através do método __len__."""
        return len(self.queque)

    def enqueue(self, value):
        """ implementar o método de inserção """
        self.queque.append(value)

    def dequeue(self):
        """ implementar o método de remoção """
        value = self.queque[0]
        del self.queque[0]
        return value

    def search(self, index):
        """ implementar o método de busca """
        if index < 0 or index > len(self.queque) - 1:
            raise IndexError()
        else:
            return self.queque[index]
