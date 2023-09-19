import sys
from itertools import combinations

nine_list=[]
for _ in range(9):
    nine_list.append(int(sys.stdin.readline()))

combi_list = combinations(nine_list,2)

for combi in combi_list:
    if sum(nine_list)-sum(combi)==100:
        nine_list.remove(combi[0])
        nine_list.remove(combi[1])
        break

nine_list.sort()

for dwarf in nine_list:
    print(dwarf)

