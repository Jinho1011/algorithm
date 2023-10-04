import sys
from collections import deque

#최단 길이를 구하기 때문에 큐에 distance 값도 함께 넘겨주어야 한다!

N,K=map(int,sys.stdin.readline().split())

if N==K:
    print(0)
    sys.exit(0)

visit=[False for _ in range(100001)]

def validSpot(nx):
    if 0<=nx<=100000:
        if visit[nx]==False:
            return True
    return False

def bfs():
    queue=deque()
    queue.append((N,0))
    visit[N]=True
    while queue:
        x,d=queue.popleft()
        if x+1==K or x-1==K or 2*x==K:
            return d+1
        if validSpot(x+1):
            queue.append((x+1,d+1))
            visit[x+1]=True
        if validSpot(x-1):
            queue.append((x-1,d+1))
            visit[x-1]=True
        if validSpot(2*x):
            queue.append((2*x,d+1))
            visit[2*x]=True

print(bfs())
