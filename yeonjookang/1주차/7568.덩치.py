import sys

N=int(sys.stdin.readline())
dungchis=[]

for _ in range(N):
    dungchis.append(list(map(int,sys.stdin.readline().split())))

for dungchi in dungchis:
    rank=1
    for compare_dungchi in dungchis:
        if dungchi[0]<compare_dungchi[0] and dungchi[1]<compare_dungchi[1]: rank+=1
    print(rank,end=" ")    


