class MyStack:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__ (self):
        self.mas = [None for i in range(10)]
        self.top = -1

    # метод добавления элемента в стек
    def push(self, elem):
        if self.top == 9:
            return False

        self.top += 1
        self.mas[self.top] = elem

        return True

    # метод удаления элемента из стека
    def pop(self):
        if (self.isEmpty()):
            return None

        elem = self.mas[self.top]
        self.mas[self.top] = None
        self.top -= 1
        return elem

    # метод определения, пуст ли стек
    def isEmpty(self):
        return self.top == -1

A = MyStack()
print(A.isEmpty())
A.push(1)
A.push(2)
print(A.pop())
A.push(3)
print(A.pop())
A.push(4)
A.push(5)
print(A.isEmpty())
A.push(6)
print(A.pop())
print(A.pop())
print(A.pop())
print(A.pop())
print(A.isEmpty())