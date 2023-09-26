import sys
N,M=map(int,sys.stdin.readline().split())

#방문 체크를 위한 1차원 배열
visit=[False for _ in range(N+1)]

#인접 행렬을 위한 2차원 배열
adj=[[] for _ in range(N+1)]

cnt=0

def dfs(num):
    visit[num]=True
    for i in adj[num]:
        if not visit[i]:
            dfs(i)

for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    #인접 행렬 정보 저장
    adj[u].append(v)
    adj[v].append(u)
    
for i in range(1,N+1):
    if not visit[i]:
        cnt+=1
        dfs(i)

print(cnt)
