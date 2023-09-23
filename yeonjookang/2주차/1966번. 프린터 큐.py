import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    important_list=list(map(int,sys.stdin.readline().split()))
    docs_deque=deque([i for i in range(N)])
    cnt=1

    while len(docs_deque)!=0 :
        pop_num = docs_deque.popleft()
        if max(important_list)!=important_list[pop_num]:
            docs_deque.append(pop_num)
        else :
            important_list[pop_num]=0
            if pop_num==M:
                print(cnt)
                break
            cnt+=1


