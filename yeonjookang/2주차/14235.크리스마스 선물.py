import sys
import heapq

n=int(sys.stdin.readline())
gift_heapq=[]

for _ in range(n):
    input=list(map(int,sys.stdin.readline().split()))

    if input[0]==0:
        if len(gift_heapq)==0:
            print(-1)
        else:
            print(-heapq.heappop(gift_heapq))
    else: 
        for i in range(input[0]):
            heapq.heappush(gift_heapq,-input[i+1])