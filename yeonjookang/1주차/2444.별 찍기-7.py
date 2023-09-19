N=int(input())

for i in range(0,N-1):
    for j in range(N-i-1):
        print(" ",end="")
    for j in range(1+i*2):
        print("*",end="")
    print()

for i in range(N*2-1):
    print("*",end="")
print()

for i in range(0,N):
    for j in range(i+1):
        print(" ",end="")
    for j in range((N-i-1)*2-1):
        print("*",end="")
    print()