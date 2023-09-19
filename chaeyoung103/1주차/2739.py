import sys

num = int(sys.stdin.readline().strip())

for i in range(9):
    result = num * (i+1)
    print(num,'*', (i+1) ,'=',result)
