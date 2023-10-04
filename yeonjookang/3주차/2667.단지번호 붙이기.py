import sys
from collections import deque

N=int(sys.stdin.readline())

#맵 정보 저장
Map=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = sys.stdin.readline().strip()
    for j in range(N):
        Map[i][j]=int(line[j])

#방분 2차원 배열
visit=[[False for _ in range(N)] for _ in range(N)]

#유효성 검사 메소드
def validSpot(ny,nx):
    if 0<=nx<N and 0<=ny<N:
        if visit[ny][nx]==False and Map[ny][nx]==1:
            return True
        else:
            return False
    else:
        return False

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
                visit[ny][nx]=True
                queue.append((ny,nx))
                cnt+=1
    return cnt

dangi_list=[]

#main 메소드
for i in range(N):
    for j in range(N):
        if visit[i][j]==False and Map[i][j]==1:
            dangi_list.append(bfs(i,j))

dangi_list.sort()

print(len(dangi_list))
for dangi in dangi_list:
    print(dangi)



