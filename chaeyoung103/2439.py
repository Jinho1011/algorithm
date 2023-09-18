import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    print(' '* (n-(i+1))+'*'*(i+1))