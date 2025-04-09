class Item:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__ (self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)

class MyList:
    # конструктор, который корректно инициализирует голову и хвост списка
    def __init__(self):
        self.head = Item(None, None, None)
        self.tail = self.head

    # метод добавления элемента в конец списка
    def append(self, data):
        item = Item(data, self.tail, None)
        self.tail.next = item
        self.tail = item

    # метод удаления элемента из конца списка (не забываем про пустой список!)
    def pop(self):
        # nothing to remove
        if self.head == self.tail:
            return None

        item = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        return item.data

    # метод добавления элемента в начало списка (помним про указатель tail!)
    def pushFirst(self, data):
        if self.head.next == None:
            item = Item(data, self.head, None)
            self.head.next = item
            self.tail = item
            return
        item = Item(data, self.head, self.head.next)
        self.head.next.prev = item
        self.head.next = item

    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if self.head == self.tail:
            return None

        item = self.head.next

        self.head.next = item.next

        if item.next != None:
            item.next.prev = self.head
        else:
            self.tail = self.head

        return item.data

    def addAfter(self, p, x):
        if p == None:
            raise Exception("Passed None item")

        next = p.next
        item = Item(x, p, next)
        p.next = item
        if next != None:
            next.prev = item
        else:
            self.tail = item

    def remove(self, p):
        if p == self.head:
            raise Exception("Tried to remove Head")
        if p == None:
            raise Exception("Tried to remove None")
        p.prev.next = p.next

        if p.next != None:
            p.next.prev = p.prev
        else:
            self.tail = p.prev

    def find(self, x):
        for elem in self:
            if elem.data == x:
                return elem
        return None

    def __getitem__(self, idx):
        if idx < 0:
            raise Exception("ID out of range")

        for i, item in enumerate(self):
            if i == idx:
                return item.data

        raise Exception("ID out of range")

    def __setitem__(self, idx, x):
        for i, item in enumerate(self):
            if i == idx:
                item.data = x

    def __contains__(self, x):
        for i in self:
            if i.data == x:
                return True
        return False

    def __add__(self, lst):
        A = MyList()

        for item in self:
            A.append(item.data)

        for item in lst:
            A.append(item.data)

        return A

    def concat(self, lst):
        if lst.head.next != None:
            self.tail.next = lst.head.next
            lst.head.next.prev = self.tail
            self.tail = lst.tail

        lst.head.next = None
        lst.tail = lst.head

    # метод определения длины списка
    def __len__(self):
        count = 0
        a = self.head
        while a.next != None:
            a = a.next
            count += 1
        return count

    # метод конструирования строкового представления списка
    def __str__(self):
        txt = "["
        a = self.head.next
        while a != None:
            if len(txt) > 1:
                txt += ", "
            txt += str(a.data)
            if a != None:
                a = a.next
        txt += "]"
        return txt

    def __iter__(self):
        return MyListIterator(self.head)

class MyListIterator:
    def __init__(self, item):
        self.currentItem = item

    def __next__(self):
        if self.currentItem.next == None:
            raise StopIteration

        self.currentItem = self.currentItem.next
        return self.currentItem

A = MyList()
A.append(1)
A.pushFirst(3)
A.append(5)
A.append(1)
A.pushFirst(5)
print(A)
print(A.popFirst())
print(A.pop())
print(A)
print(len(A))
if (1 in A):
	print("True")
else:
    print("False")
if (2 in A):
	print("True")
else:
    print("False")
for i in range(6,10):
    A.append(i)
A[0] = 0
A[4] = -1
for i in range(len(A)):
    print(A[i])
for id, i in enumerate(A):
	print(i)
	print(A[id])