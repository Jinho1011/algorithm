import sys
import heapq

N,M=map(int,sys.stdin.readline().split())

gift_list=list(map(int,sys.stdin.readline().split()))
gift_heapq=[]

children_list=list(map(int,sys.stdin.readline().split()))

#이미 생성해둔 리스트가 있다면 heapify 함수 이용
#heapq.heapify(gift_list)

#최대힙 정렬
for gift in gift_list:
    heapq.heappush(gift_heapq,-gift)

for child in children_list:
    pop=-heapq.heappop(gift_heapq)
    if pop>=child:
        pop-=child
        heapq.heappush(gift_heapq,-pop)
    else:
        print(0)
        sys.exit()
print(1)
