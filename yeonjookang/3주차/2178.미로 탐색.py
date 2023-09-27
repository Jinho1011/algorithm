import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

#N행 M열 맵 생성
Map=[[chr for chr in sys.stdin.readline().strip()] for _ in range(N)]

#방문 체크 2차원 배열 생성
visit=[[False for _ in range(M)] for _ in range(N)]

#네 방향 체크
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#유효한 위치인지 체크
def validSpot(x,y):
    if x>=0 and x<=M-1 and y>=0 and y<=N-1 and visit[y][x]==False:
        return True
    else:
        return False

#bfs 함수 정의
def bfs():
    queue=deque()
    visit[0][0]=True
    queue.append((0,0,1))
    while 1:
        x,y,d=queue.popleft()
        if x==M-1 and y==N-1:
            return d
        else:
            d+=1
            for i in range(4):
                n_x=x+dx[i]
                n_y=y+dy[i]
                if validSpot(n_x,n_y):
                    if Map[n_y][n_x]=='1':
                        queue.append((n_x,n_y,d))
                        visit[n_y][n_x]=True

print(bfs())


