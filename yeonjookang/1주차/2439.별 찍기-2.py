N = int(input())

for i in range(0,N):
    for j in range(N-1-i):
        print(' ',end="")
    for j in range(i+1):
        print('*',end="")
    print()