import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque(range(1, N+1))

new_list = []

for i in range(N):
    queue.rotate(-(K-1))
    new_list.append(queue.popleft())


print(str(new_list).replace('[', '<').replace(']', '>'))