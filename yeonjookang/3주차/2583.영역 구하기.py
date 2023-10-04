import sys
from collections import deque

M,N,K=map(int,sys.stdin.readline().split())

#Map 2차원 배열
Map=[[1 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    left_x,left_y,right_x,right_y=map(int,sys.stdin.readline().split())
    for i in range(left_y,right_y):
        for j in range(left_x,right_x):
            Map[i][j]=0

#visit 2차원 배열
visit=[[False for _ in range(N)] for _ in range(M)]

#유효성 검사 메소드
def validSpot(spot_y,spot_x):
    if 0<=spot_x<N and 0<=spot_y<M:
        if visit[spot_y][spot_x]==False and Map[spot_y][spot_x]==1:
            return True
        else: return False
    else: return False

#네 방향 배열
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#bfs 메소드
def bfs(spot_y,spot_x):
    visit[spot_y][spot_x]=True
    cnt=1
    queue=deque()
    queue.append((spot_y,spot_x))
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if validSpot(ny,nx):
                queue.append((ny,nx))
                visit[ny][nx]=True
                cnt+=1
    return cnt

domain_list=[]

#메인 메소드
for i in range(M):
    for j in range(N):
        if visit[i][j]==False and Map[i][j]==1:
            domain_list.append(bfs(i,j))

print(len(domain_list))
domain_list.sort()

for domain in domain_list:
    print(domain,end=" ")