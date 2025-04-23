from collections import deque

operations = ["+", "-", "*", "/", "**"]

def stringify(root):
    if root == None:
        return "()"
    if type(root) != list:
        return str(root)

    return f"({stringify(root[0])} {stringify(root[1])} {stringify(root[2])})"

def calculate(symbols):
    s = deque()
    for i in symbols:
        if i in operations:
            if len(s) < 2:
                return "error"
            b = s.pop()
            a = s.pop()
            s.append([i, a, b])
        else:
            s.append([i, None, None])

    if len(s) != 1:
        return "error"

    return s.pop()

operators = ['+','-','*','/','**']

priorities = {
    '+':2,
    '-':2,
    '*':3,
    '/':3,
    '**':4,
}

def convert(symbols):
    text = ""

    queue = deque()
    stack = deque()

    for i in symbols:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while len(stack) != 0 and stack[-1] != '(':
                if len(stack) == 1 and stack[-1] != '(':
                    return "error"
                queue.appendleft(stack.pop())
            stack.pop()
        elif i in operators:
            priority = priorities[i]
            if len(stack) == 0 or stack[-1] == '(':
                stack.append(i)
            elif stack[-1] in operators and priorities[stack[-1]] < priority:
                stack.append(i)
            else:
                while True:
                    if len(stack) == 0:
                        break
                    if stack[-1] not in operators:
                        break
                    if priorities[stack[-1]] > priority or (priorities[stack[-1]] == priority and stack[-1] != "**"):
                        queue.appendleft(stack.pop())
                    else:
                        break
                stack.append(i)
        else:
            queue.appendleft(i)  # number
    while len(stack) > 0:
        if stack[-1] == '(':
            return "error"
        queue.appendleft(stack.pop())

    result = []

    while len(queue) > 0:
        result.append(queue.pop())
    return result