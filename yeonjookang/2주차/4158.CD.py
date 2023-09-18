import sys

while 1:
    N,M=map(int,sys.stdin.readline().split())

    if N==0 and M==0:
        sys.exit()

    cd_set1=set()
    cd_set2=set()

    for _ in range(N):
        cd_set1.add(int(sys.stdin.readline()))
    for _ in range(M):
        cd_set2.add(int(sys.stdin.readline()))

    print(len(cd_set1&cd_set2))
