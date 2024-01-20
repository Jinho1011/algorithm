import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    input_str = sys.stdin.readline()
    if input_str.startswith("push"):
        stack.append(input_str.split()[1])
    if input_str.startswith("pop"):
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    if input_str.startswith("size"):
        print(len(stack))
    if input_str.startswith("empty"):
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    if input_str.startswith("top"):
        if len(stack)!=0:
            print(stack[len(stack)-1])
        else:
            print(-1)