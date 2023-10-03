import sys
from collections import deque

N,M,K=map(int,sys.stdin.readline().split())

#방문 체크 2차원 배열
visit=[[False for _ in range(M+1)] for _ in range(N+1)]

#Map 2차원 배열
Map=[['.' for _ in range(M+1)] for _ in range(N+1)]

for _ in range(K):
    r,c=map(int,sys.stdin.readline().split())
    Map[r][c]='*'

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def validSpot(nx,ny):
    if 0<nx<=M and 0<ny<=N:
        if Map[ny][nx]=="*" and visit[ny][nx]==False:
            return True
        else:
            return False
    else:
        return False

#bfs 
def bfs(n,m):
    visit[n][m]=True
    queue=deque()
    queue.append((n,m))
    result=1
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if validSpot(nx,ny):
                queue.append((ny,nx))
                Map[ny][nx]=True
                result+=1
    return result

answer=0
for i in range(1,N+1):
    for j in range(1,M+1):
        if visit[i][j]==False and Map[i][j]=='*':
            result = bfs(i,j)
            answer=max(result,answer)
        
print(answer)

    