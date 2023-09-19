import sys
from collections import deque

N = int(sys.stdin.readline().strip())

card_list = deque(range(1, N+1))
card_list2 = deque()



for i in range(N):
    card_list2.appendleft(card_list.pop())
    card_list2.rotate(N-i)

print(*card_list2)