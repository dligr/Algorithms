from collections import deque

operations = ["+", "-", "*", "/", "**"]

def calculate(symbols):
    s = deque()
    for i in symbols:
        if i in operations:
            if len(s) < 2:
                return "error"
            b = int(s.pop())
            a = int(s.pop())
            c = None
            if i == '+':
                c = a + b
            elif i == '-':
                c = a - b
            elif i == '*':
                c = a * b
            elif i == '/':
                c = a // b
            elif i == '**':
                c = a ** b
            s.append(str(c))
        else:
            s.append(i)

    if len(s) != 1:
        return "error"

    return s.pop()