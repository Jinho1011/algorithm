import sys
from collections import deque

N = int(sys.stdin.readline().strip())

card_list = deque(range(1, N+1))

while True:
    if len(card_list) > 1:
        card_list.popleft()
    else:
        break
    if len(card_list) == 1:
        break
    pop_card = card_list.popleft()
    card_list.append(pop_card)

print(card_list[0])