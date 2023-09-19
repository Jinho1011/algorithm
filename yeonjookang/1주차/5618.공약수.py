import sys

N = int(sys.stdin.readline())

if N ==2 :
    A,B=map(int,sys.stdin.readline().split())
    for i in range(1,min(A,B)+1):
        if A%i==0 and B%i==0:
            print(i)
else:
    A,B,C=map(int,sys.stdin.readline().split())
    for i in range(1,min(A,B,C)+1):
        if A%i==0 and B%i==0 and C%i==0:
            print(i)