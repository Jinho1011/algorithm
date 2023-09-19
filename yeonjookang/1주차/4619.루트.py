import sys

while 1:
    B,N=map(int,sys.stdin.readline().split())
    if B==0: sys.exit()
    elif B==1: print(1)
    elif N==1: print(B)
    else:
        for i in range(2,B+1):
            A_N=i**N
            if A_N>B:
                if min(A_N-B,B-(i-1)**N) == A_N-B:
                    print(i)
                    flag=1
                    break
                else:
                    print(i-1)
                    flag=1
                    break
    
    
