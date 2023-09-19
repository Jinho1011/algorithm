import sys
import heapq

N, M = map(int,sys.stdin.readline().split())

gift = list(map(lambda x: -int(x), sys.stdin.readline().split()))
child = list(map(int,sys.stdin.readline().split()))
result = 1

heapq.heapify(gift)

for i in range(M):
    max_gift = -heapq.heappop(gift)
    if max_gift < child[i]:
        result = 0
        break
    else:
        temp = max_gift - child[i]
        heapq.heappush(gift, -temp)

print(result)