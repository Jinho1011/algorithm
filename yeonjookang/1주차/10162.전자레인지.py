import sys

T = int(sys.stdin.readline())

A=T//300
B=(T-300*A)//60
C=(T-300*A-60*B)//10
if T-300*A-60*B-10*C==0:
    print(f'{A} {B} {C}')
else:
    print(-1)

