import sys
from collections import deque

N=int(sys.stdin.readline())
deque=deque()

for i in range(1,N+1):
    deque.append(i)

flag=0
while len(deque)!=1:
    if flag==0:
        deque.popleft()
        flag=1
    else:
        top=deque.popleft()
        deque.append(top)
        flag=0
print(deque.pop())