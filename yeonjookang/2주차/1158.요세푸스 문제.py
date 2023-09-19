import sys
N,K=map(int,sys.stdin.readline().split())

round_list=[]

for i in range(1,N+1):
    round_list.append(i)

answer_list=[]
index=0

for _ in range(N):
    cnt=0
    while 1:
        if index>N-1: index=0
        if round_list[index]!=0:
            cnt+=1
        if cnt==K:
            answer_list.append(round_list[index])
            round_list[index]=0
            break
        index+=1
print('<',end='')
for i in range(N):
    if i==N-1: print(answer_list[i],end='')
    else: print(f'{answer_list[i]}, ',end='')
print('>',end='')
