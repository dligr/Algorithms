import unittest
from RPN import calculate
from shunting_yard import convert
from DFS import walk_around_prefix
from DFS import walk_around_postfix
from SAT import convert as convert_SAT
from SAT import calculate as calculate_SAT
from SAT import stringify

class MyTestCase(unittest.TestCase):
    def test_RPN(self):
        self.assertEqual(calculate(["2", "2", "+"]), "4")
        self.assertEqual(calculate(["2", "2", "-"]), "0")
        self.assertEqual(calculate(["2", "5", "*"]), "10")
        self.assertEqual(calculate(["22", "2", "/"]), "11")
        self.assertEqual(calculate(["2", "4", "**"]), "16")

        self.assertEqual(calculate(["2", "4", "+", "2", "*"]), "12")
        self.assertEqual(calculate(["2"]), "2")
        self.assertEqual(calculate(["2", "*"]), "error")
        self.assertEqual(calculate(["*"]), "error")
    def test_shunting_yard(self):
        self.assertEqual(convert(["2", "+", "2"]), "2 2 +")
        self.assertEqual(convert(["5", "+", "2", "*", "3"]), "5 2 3 * +")
        self.assertEqual(convert(["5", "+", "2", "**", "3"]), "5 2 3 ** +")
        self.assertEqual(convert(["(", "5", "+", "2", ")", "**", "3"]), "5 2 + 3 **")
        self.assertEqual(convert(["25"]), "25")
        self.assertEqual(convert(["(", "2"]), "error")
    def test_DFS(self):
        self.assertEqual(
            walk_around_prefix(5, [(1, 2), (2, 3), (2, 5), (5, 9), (9, 7), (7, 6), (7, 8), (9, 10)], result=[]),
            [5, 2, 1, 3, 9, 7, 6, 8, 10]
        )
        self.assertEqual(
            walk_around_postfix(5, [(1, 2), (2, 3), (2, 5), (5, 9), (9, 7), (7, 6), (7, 8), (9, 10)], result=[]),
            [1, 3, 2, 6, 8, 7, 10, 9, 5]
        )
        self.assertEqual(walk_around_prefix(5, [(5, 4)], result=[]),
                         [5, 4])
        self.assertEqual(walk_around_postfix(5, [(5, 4)], result=[]),
                         [4, 5])
        self.assertEqual(walk_around_prefix(5, [], result=[]),
                         [5])
        self.assertEqual(walk_around_postfix(5, [], result=[]),
                         [5])
    def test_SAT(self):
        self.assertEqual(stringify(calculate_SAT(convert_SAT("2 + 3 * 4 - 5".split(' ')))),
                         "(- (+ (2 () ()) (* (3 () ()) (4 () ()))) (5 () ()))")
        self.assertEqual(stringify(calculate_SAT(convert_SAT("2 + 3".split(' ')))),
                         "(+ (2 () ()) (3 () ()))")



if __name__ == '__main__':
    unittest.main()
