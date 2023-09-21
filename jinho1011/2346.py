from collections import deque
from sys import stdin

N = int(stdin.readline())
numbers = stdin.readline().split()
numbers = deque((int(number), index + 1) for index, number in enumerate(numbers))

answer = []

while len(numbers)>0:
    target = numbers.popleft()
    answer.append(target[1])

    if len(numbers) == 1:
        target = numbers.popleft()
        answer.append(target[1])
        break
    
    for i in range(abs(target[0]) if target[0] < 0 else abs(target[0])-1):
        numbers.appendleft(numbers.pop()) if target[0] < 0 else numbers.append(numbers.popleft())

for a in answer: print(a, end=' ')
        
