from collections import deque

operations = ["+", "-", "*", "/", "**"]

def findHeight(root):
    if type(root) != list:
        return 0
    return 1 + max(findHeight(root[1]), findHeight(root[2]))

def fillInMatrix(root, matrix, height, layer=0, horizontal=-1):
    if horizontal == -1:
        horizontal = 2 ** (height - layer - 1) - 1

    coords = (layer * 3, horizontal)

    matrix[coords[0]][coords[1]] = str(root[0])

    if type(root) != list:
        return coords

    if root[1] == None and root[2] == None:
        return coords

    matrix[coords[0] + 1][coords[1]] = "|"

    if root[1] != None:
        a = fillInMatrix(root[1], matrix, height, layer + 1, horizontal - 2 ** (height - layer - 2))
    else:
        a = coords
    if root[2] != None:
        b = fillInMatrix(root[2], matrix, height, layer + 1, horizontal + 2 ** (height - layer - 2))
    else:
        b = coords

    for i in range(a[1], b[1] + 1):
        matrix[coords[0] + 2][i] = "-"

    return coords

def stringify(root):
    h = findHeight(root)

    matrix = [[" " for i in range(2 ** h - 1)] for i in range(3*h + 1)]

    fillInMatrix(root, matrix, h)

    for i in matrix:
        for j in reversed(range(len(i))):
            if i[j] != " ":
                break
            i[j] = None

    matrix[0][0] = "."

    s = ""

    for i in matrix:
        for j in i:
            if j == None:
                break
            s += j
        s += "\n"
    return s

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


symbols = input().split(' ')

RPN = convert(symbols)

root = calculate(RPN)

print(stringify(root))