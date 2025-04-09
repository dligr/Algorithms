import unittest
from stack import MyStack


class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = MyStack()
        self.assertEqual(A.mas, [None for i in range(10)])
        self.assertEqual(A.top, -1)
        A.push(1)
        self.assertEqual(A.top, 0)
        A.push(2)
        A.push(3)
        self.assertEqual(A.top, 2)
        self.assertEqual(A.pop(), 3)
        self.assertEqual(A.pop(), 2)
        self.assertEqual(A.pop(), 1)
        self.assertEqual(A.top, -1)
        self.assertEqual(A.pop(), None)
        self.assertEqual(A.top, -1)


if __name__ == '__main__':
    unittest.main()
