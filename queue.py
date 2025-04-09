class MyQueue:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.mas = [None for i in range(10)]
        self.tail = -1
        self.head = 0
        self.isFull = False

    # метод добавления элемента в очередь
    def enqueue(self, elem):
        if self.tail == self.head - 1 and self.isFull:
            return False

        self.tail += 1

        if self.tail == 9:
            self.tail = -1

        self.mas[self.tail] = elem

        if self.tail == self.head - 1:
            self.isFull = True

        return True

    # метод удаления элемента из очереди
    def dequeue(self):
        if self.isEmpty():
            return None

        elem = self.mas[self.head]
        self.mas[self.head] = None
        self.head += 1

        if self.head == 10:
            self.head = 0

        self.isFull = False

        return elem

    # метод для определения, пуста ли очередь
    def isEmpty(self):
        return self.tail == self.head - 1 and not self.isFull

# Этот код менять не нужно. При корректной реализации класса MyQueue он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
A = MyQueue()
print(A.isEmpty())
A.enqueue(1)
A.enqueue(2)
print(A.dequeue())
A.enqueue(3)
print(A.dequeue())
A.enqueue(4)
A.enqueue(5)
print(A.isEmpty())
A.enqueue(6)
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.isEmpty())
A.enqueue(10)
A.enqueue(11)
A.enqueue(12)
A.enqueue(13)
A.enqueue(14)
A.enqueue(15)
A.enqueue(16)
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())