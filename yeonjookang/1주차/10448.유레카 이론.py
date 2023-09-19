import sys
from itertools import combinations_with_replacement

N=int(sys.stdin.readline())

T_N=[]
for i in range(1,45):
    T_N.append(int(i*(i+1)/2))

for _ in range(N):
    flag=0
    input_num=int(sys.stdin.readline())
    for combi in combinations_with_replacement(T_N,3):
        if sum(combi)==input_num:
            print(1)
            flag=1
            break
    if flag==0:
        print(0)
    
