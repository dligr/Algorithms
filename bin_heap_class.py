# не забудьте про аннотирование типов!

import math

class Heap:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.heap = []

    def left_son(self, p: int) -> int:
        level = math.floor(math.log2(p + 1))
        relative_id = p - 2 ** level + 1

        return 2 ** (level + 1) - 1 + relative_id * 2

    def right_son(self, p: int) -> int:
        return self.left_son(p) + 1

    def min_son(self, p: int) -> int:
        # возвращаем индекс минимального сына элемента p или -1, если p - лист
        left = self.left_son(p)
        if left >= len(self.heap):
            return -1

        if left + 1 >= len(self.heap):
            return left

        if self.heap[left] < self.heap[left + 1]:
            return left
        else:
            return left + 1

    def parent(self, p: int) -> int:
        if p == 0:
            return 0

        level = math.floor(math.log2(p + 1))
        relative_id = p - 2 ** level + 1

        return 2**(level - 1) + relative_id // 2 - 1

    def sift_up(self, p: int):
        # если мы в корне, то выходим
        if p == 0:
            return

        # пока мы не в корне и текущий элемент меньше родительского, меняем их и поднимаемся выше
        while self.heap[p] < self.heap[self.parent(p)] and p != 0:
            self.heap[p], self.heap[self.parent(p)] = self.heap[self.parent(p)], self.heap[p]
            p = self.parent(p)

    def sift_down(self, p: int):
        minCh = self.min_son(p)
        # пока мы не в листе и текущий элемент больше минимального из сыновей,
        # меняем их местами и погружаемся ниже
        while minCh != -1 and self.heap[p] > self.heap[minCh]:
            self.heap[p], self.heap[minCh] = self.heap[minCh], self.heap[p]
            p = minCh
            minCh = self.min_son(p)

    # метод для добавления элемента x в кучу
    def add(self, elem: int):
        self.heap.append(elem)
        self.sift_up(len(self.heap) - 1)

    # метод для возврата минимума
    def min(self) -> int:
        return self.heap[0]

    # метод для возврата минимума и удаления его из кучи
    def get_min(self) -> int:
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        min = self.heap.pop(len(self.heap) - 1)
        self.sift_down(0)

        return min

    # печать массива с бинарным деревом кучи
    def __str__(self) -> str:
        result = ""
        for i, elem in enumerate(self.heap):
            if i != 0:
                result += " "
            result += str(elem)
        return result