import sys
from collections import deque

N=int(sys.stdin.readline())

deque=deque()
deque.append(N)
n=N

for i in range(N-1,0,-1):
    deque.append(i)
    for j in range(i):
        pop=deque.popleft()
        deque.append(pop)

for _ in range(len(deque)):
    print(deque.pop(),end=' ')