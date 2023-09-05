n=int(input())
for i in range(n):
    R,S=map(str,input().split())
    R=int(R)
    for c in S:
        for _ in range(R):
            print(c,end="")
    print()