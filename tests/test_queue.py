import unittest
from queue import MyQueue


class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = MyQueue()
        self.assertEqual(A.head, 0)
        self.assertEqual(A.tail, -1)
        self.assertEqual(A.mas, [None for i in range(10)])

        self.assertEqual(A.isEmpty(), True)
        A.enqueue(10)
        self.assertEqual(A.isEmpty(), False)
        self.assertEqual(A.dequeue(), 10)
        self.assertEqual(A.dequeue(), None)
        for i in range(10):
            A.enqueue(i)
        for i in range(10):
            self.assertEqual(A.dequeue(), i)


if __name__ == '__main__':
    unittest.main()
