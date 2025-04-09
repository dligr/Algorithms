import unittest
from linked_list import MyList

class MyTestCase(unittest.TestCase):
    def test_positive(self):
        A = MyList()
        A.append(3)
        self.assertEqual(len(A), 1)
        self.assertEqual(str(A), "[3]")
        A.append(25)
        self.assertEqual(len(A), 2)
        self.assertEqual(str(A), "[3, 25]")
        A.pushFirst(5)
        self.assertEqual(len(A), 3)
        self.assertEqual(str(A), "[5, 3, 25]")

        self.assertEqual(A.popFirst(), 5)
        self.assertEqual(len(A), 2)
        self.assertEqual(str(A), "[3, 25]")

        self.assertEqual(A.pop(), 25)
        self.assertEqual(len(A), 1)
        self.assertEqual(str(A), "[3]")
        A.append(25)
        self.assertEqual(len(A), 2)
        self.assertEqual(str(A), "[3, 25]")
        A.pushFirst(5)
        self.assertEqual(len(A), 3)
        self.assertEqual(str(A), "[5, 3, 25]")

        B = MyList()

        for i in range(10):
            B.append(i)
        self.assertEqual(B[0], 0)
        self.assertEqual(B[2], 2)
        self.assertEqual(B[1], 1)
        self.assertEqual(B[5], 5)

        A.concat(B)

        self.assertEqual(len(A), 13)

    def test_corner_cases(self):
        A = MyList()
        self.assertEqual(len(A), 0)
        self.assertEqual(str(A), "[]")

        self.assertEqual(A.pop(), None)
        self.assertEqual(len(A), 0)
        self.assertEqual(str(A), "[]")

        self.assertEqual(A.popFirst(), None)
        self.assertEqual(len(A), 0)
        self.assertEqual(str(A), "[]")

        A.append(2)
        self.assertEqual(A.pop(), 2)
        self.assertEqual(len(A), 0)
        self.assertEqual(str(A), "[]")

        B = MyList()
        B.append(25)
        self.assertEqual(B[0], 25)
        B[0] = 100
        self.assertEqual(B[0], 100)

        for i in B:
            self.assertEqual(i.data, 100)

        firstB = B.head.next
        lastA = A.tail
        A.concat(B)

        self.assertEqual(firstB.prev, lastA)
        self.assertEqual(firstB, lastA.next)


if __name__ == '__main__':
    unittest.main()
