import sys

N=int(sys.stdin.readline())
stack=[]
stack_size=0

def push(x):
    global stack_size
    stack.append(x)
    stack_size+=1
def pop():
    global stack_size
    if stack_size==0:
        return -1
    stack_size-=1
    return stack.pop()
def size():
    global stack_size
    return stack_size
def empty():
    global stack_size
    if stack_size==0:
        return 1
    return 0
def top():
    global stack_size
    if stack_size==0:
        return -1
    return stack[stack_size-1]

for _ in range(N):
    input_str=sys.stdin.readline().strip()
    if input_str.startswith("push"):
        x=(input_str.split(" "))[1]
        push(x)
    if input_str=="pop":
        print(pop())
    if input_str=="size":
        print(size())
    if input_str=="empty":
        print(empty())
    if input_str=="top":
        print(top())
