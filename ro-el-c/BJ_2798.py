import sys
input = sys.stdin.readline
import itertools

n, m = map(int, input().split())

cardNum = list(map(int, input().split()))

max = 0

comb = list(map(list, itertools.combinations(cardNum, 3)))
for tmp in comb:
    tmpSum = sum(tmp)
    if tmpSum <= m and tmpSum > max:
        max = tmpSum

print(max)