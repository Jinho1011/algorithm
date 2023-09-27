import sys
from itertools import combinations

N,S=map(int,sys.stdin.readline().split())

num_list=list(map(int,sys.stdin.readline().split()))

cnt=0
for i in range(1,N+1):
    for combi in combinations(num_list,i):
        if sum(combi)==S: cnt+=1

print(cnt)



