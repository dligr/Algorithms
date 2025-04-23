from collections import deque

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

    result = ""

    i = 0
    while len(queue) > 0:
        if i != 0:
            result += " "
        result += queue.pop()
        i += 1
    return result