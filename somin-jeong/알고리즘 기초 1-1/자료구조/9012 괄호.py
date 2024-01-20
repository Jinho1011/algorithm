import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    input_str = sys.stdin.readline().replace("\n", "")
    for char in input_str:
        if char == '(':
            stack.append(char)
        elif char == ')' and len(stack) != 0:     # stack에 '(' 가 있을 때
            stack.pop()
        else:                                     # stack에 '('가 없는데 ')'가 나올 때    # '('의 개수 < ')'의 개수
            stack.append(char)
            break
    if len(stack) != 0:
        print("NO")
    else:
        print("YES")
    stack.clear()
    