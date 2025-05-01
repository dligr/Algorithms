import unittest
from bin_heap_funcs import parent
from bin_heap_funcs import sift_up

from bin_heap_funcs import left_son
from bin_heap_funcs import right_son
from bin_heap_funcs import min_son
from bin_heap_funcs import sift_down

from bin_heap_class import Heap

class MyTestCase(unittest.TestCase):
    def test_funcs(self):
        self.assertEqual(parent(7), 3)
        self.assertEqual(parent(8), 3)
        self.assertEqual(parent(9), 4)
        self.assertEqual(parent(0), 0)
        self.assertEqual(parent(1), 0)
        self.assertEqual(parent(2), 0)
        self.assertEqual(parent(1024), 511)
        self.assertEqual(parent(4096), 2047)
        self.assertEqual(parent(8192), 4095)

        heap = [1, 10, 8, 32, 11, 38, 42, 78, 31]
        sift_up(heap, 8)
        self.assertEqual(heap, [1, 10, 8, 31, 11, 38, 42, 78, 32])
        heap = [1, 2, 0]
        sift_up(heap, 2)
        self.assertEqual(heap, [0, 2, 1])
        sift_up(heap, 2)
        self.assertEqual(heap, [0, 2, 1])

        heap = [5, 1, 2]
        sift_down(heap, 0)
        self.assertEqual(heap, [1, 5, 2])

        self.assertEqual(min_son(heap, 0), 2)

        self.assertEqual(left_son(0), 1)
        self.assertEqual(right_son(0), 2)

        self.assertEqual(left_son(3), 7)
        self.assertEqual(right_son(3), 8)

    def test_class(self):
        heap = Heap()
        heap.add(1)
        heap.add(10)
        heap.add(8)
        self.assertEqual(str(heap), "1 10 8")
        heap.add(32)
        heap.add(11)
        self.assertEqual(str(heap), "1 10 8 32 11")
        heap.add(38)
        heap.add(42)
        heap.add(78)
        heap.add(31)
        self.assertEqual(str(heap), "1 10 8 31 11 38 42 78 32")
        self.assertEqual(heap.get_min(), 1)
        self.assertEqual(str(heap), "8 10 32 31 11 38 42 78")

if __name__ == '__main__':
    unittest.main()
