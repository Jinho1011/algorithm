import sys

N=int(input())

pac=1
if(N==0):
    print(1)
    sys.exit(0)

for i in range(1,N+1):
    pac=pac*i
    
print(pac)