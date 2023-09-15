import sys

n = int(sys.stdin.readline().strip())

for i in range(n*2):
    if i+1 <=n:
        print(' '* (n-(i+1))+'*'*(2*(i+1)-1)) 
    else:
        k = n*2 - (i+1)
        print(' '* (n-k)+'*'*(2*k-1))