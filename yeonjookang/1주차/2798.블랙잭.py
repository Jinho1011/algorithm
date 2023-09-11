import sys
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())

nums=map(int,sys.stdin.readline().split())

combi_list = combinations(nums,3)

answer = 0

for combi in combi_list:
    if sum(combi)<=M and answer<sum(combi):
        answer=sum(combi)

print(answer)
