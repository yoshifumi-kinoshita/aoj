from sys import stdin

a = stdin.readline().rstrip().split()

stack = []

for i in a:
    if i.isnumeric():
        stack.append(int(i))
    else:
        v2 = stack.pop()
        v1 = stack.pop()
        if i == '+':
            stack.append(v1 + v2)
        elif i == '-':
            stack.append(v1 - v2)
        elif i == '*':
            stack.append(v1 * v2)

print(stack.pop())



