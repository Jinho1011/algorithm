import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

#N행 M열 맵 제작
Map=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

#방문 체크 2차원 배열
visited = [[False]*M for _ in range(N)]

#북서남동 방향
dy=[-1,0,1,0]
dx=[0,-1,0,1]

#유효한 범위인지에 대한 함수 정의
def is_valid_coord(y,x):
    return x>=0 and y>=0 and x<M and y<N

#bfs 정의
def bfs():
    #큐 선언
    queue=deque()
    visited[0][0]=True
    #넘기는 값, y,x,현재 거리값
    queue.append((0,0,1))
    while 1:
        y,x,d=queue.pop()
        if y==N-1 and x==M-1:
            return d
        #네 방향 모두 체크
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_valid_coord(n_y,n_x):
                if not visited[n_y][n_x] and Map[n_y][n_x]=='1':
                    queue.append((n_y,n_x,d+1))
                    visited[n_y][n_x]=True
print(bfs())