
import math

def parent(p : int) -> int:
    if p == 0:
        return 0

    level = math.floor(math.log2(p + 1))
    relative_id = p - 2 ** level + 1

    return 2 ** (level - 1) + relative_id // 2 - 1

def sift_up(heap : list, p : int):
    # если мы в корне, то выходим
    if p == 0:
        return

    # пока мы не в корне и текущий элемент меньше родительского, меняем их и поднимаемся выше
    while heap[p] < heap[parent(p)] and p != 0:
        heap[p], heap[parent(p)] = heap[parent(p)], heap[p]
        p = parent(p)

def left_son(p : int) -> int:
    level = math.floor(math.log2(p + 1))
    relative_id = p - 2**level + 1

    return 2**(level + 1) - 1 + relative_id * 2

def right_son(p : int) -> int:
    return left_son(p) + 1

def min_son(heap : list, p : int) -> int:
    # возвращаем индекс минимального сына элемента p или -1, если p - лист
    left = left_son(p)
    if left >= len(heap):
        return -1

    if heap[left] < heap[left + 1]:
        return left
    else:
        return left + 1

def sift_down(heap : list, p : int):
    minCh = min_son(heap, p)
    # пока мы не в листе и текущий элемент больше минимального из сыновей,
    # меняем их местами и погружаемся ниже
    while minCh != -1 and heap[p] > heap[minCh]:
        heap[p], heap[minCh] = heap[minCh], heap[p]
        p = minCh
        minCh = min_son(heap, p)