from collections import deque


N, M = list(map(int, input().split()))
ids = list(map(int, input().split()))
dq = deque([i for i in range(1, N+1)])
cnt = 0

for id in ids:
    while True:
        if id == dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(id) <= len(dq)/2:
                dq.append(dq.popleft())
                cnt+=1
            else:
                dq.appendleft(dq.pop())
                cnt+=1

print(cnt)