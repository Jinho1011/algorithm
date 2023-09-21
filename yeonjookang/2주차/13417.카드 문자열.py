import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    possible_str=[]
    
    N=int(sys.stdin.readline())
    input_deque=deque(map(str,sys.stdin.readline().split()))
    
    for _ in range(N):
        alphabet=input_deque.popleft()

        if len(possible_str)==0:
            possible_str.append(alphabet)
        else:
            possible_str=list(possible_str)
            possible_str.sort()
            first_str=possible_str[0]
            possible_str.clear()

            possible_str.append(alphabet+first_str)
            possible_str.append(first_str+alphabet)
       
    possible_str=list(possible_str)
    possible_str.sort()
    print(possible_str[0])

        


