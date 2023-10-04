import sys
from collections import deque

N=int(sys.stdin.readline())

#Map 2차원 배열
Map=[[0 for _ in range(N)] for _ in range(N)]
max_height=0

for i in range(N):
    line_list=list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        Map[i][j]=line_list[j]
        max_height=max(max_height,line_list[j])

#visit 2차원 배열
visit=[[False for _ in range(N)] for _ in range(N)]

#유효성 검사 메소드
def validSpot(spot_y,spot_x,height):
    if 0<=spot_x<N and 0<=spot_y<N:
        if visit[spot_y][spot_x]==False and Map[spot_y][spot_x]>height:
            return True
        else: return False
    else: return False

#네 방향 배열
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#bfs 메소드
def bfs(spot_y,spot_x,height):
    visit[spot_y][spot_x]=True
    queue=deque()
    queue.append((spot_y,spot_x))
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if validSpot(ny,nx,height):
                queue.append((ny,nx))
                visit[ny][nx]=True
    return 

safe_count_list=[]

#메인 메소드
for i in range(0,max_height):
    cnt=0
    for j in range(N):
        for s in range(N):
            if visit[j][s]==False and Map[j][s]>i:
                cnt+=1
                bfs(j,s,i)
    safe_count_list.append(cnt)
    visit=[[False for _ in range(N)] for _ in range(N)]

print(max(safe_count_list))