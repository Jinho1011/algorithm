import sys
import collections

N = int(sys.stdin.readline())
queue=collections.deque()

for _ in range(N):
    input_str=sys.stdin.readline().strip().split(' ')
    cmd=input_str[0]
    if cmd=="push":
        value=int(input_str[1])
        queue.append(value)
    if cmd=="pop":
        if len(queue)!=0:
            print(queue.popleft())
        else:
            print(-1)
    if cmd=="size":
        print(len(queue))
    if cmd=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    if cmd=="front":
        if len(queue)==0:
            print(-1)
        else:
            tmp=queue.popleft()
            print(tmp)
            queue.appendleft(tmp)
    if cmd=="back":
        if len(queue)==0:
            print(-1)
        else:
            tmp=queue.pop()
            print(tmp)
            queue.append(tmp)