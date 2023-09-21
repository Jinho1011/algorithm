from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

queue = deque(range(1,N+1))
location = list(map(int,sys.stdin.readline().split()))
count = 0

for i in location:
    idx = queue.index(i) + 1
    a = idx -1 
    b = len(queue) - idx +1
    if a < b:
        queue.rotate(-a)
        count += a
    else:
        queue.rotate(b)
        count += b
    queue.popleft()

print(count)

    
