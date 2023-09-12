import sys

N=int(sys.stdin.readline())
answer=0

for i in range(1,N+1):
    if N == sum(map(int,list(str(i))))+i :
        if answer !=0: 
            if answer>i:
                answer=i
        else: answer = i
print(answer)