import sys
import itertools
input = sys.stdin.readline

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))
total = sum(dwarfs)

combList = list(map(list, itertools.combinations(dwarfs, 7)))
for tempComb in combList:
    combSum = sum(tempComb)
    if combSum == 100:
        for dwarf in tempComb:
            print(dwarf)
        sys.exit()


"""
난쟁이 9
모자에 100보다 작은 양의 정수
모자의 합이 100

9C7 = 9C2 -> Brute Force
"""