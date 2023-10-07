import sys

LEFT_ARROW = '<'
RIGHT_ARROW = '>'
DELETE = '-'

N = int(sys.stdin.readline().strip())

for i in range(N):
    keylog = sys.stdin.readline().strip()
    l_stack = []
    r_stack = []

    for key in keylog:
        if key == LEFT_ARROW:
            if l_stack:
                r_stack.append(l_stack.pop())
        elif key == RIGHT_ARROW:
            if r_stack:
                l_stack.append(r_stack.pop())
        elif key == DELETE:
            if l_stack:
                l_stack.pop()
        else:
            l_stack.append(key)
    l_stack.extend(reversed(r_stack))
    print(''.join(l_stack))
