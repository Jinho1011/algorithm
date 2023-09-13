import sys

N,K=map(int,sys.stdin.readline().split())

gugudan=[]

for i in range(1,K+1):
    gugudan.append(int(''.join(list(str(N*i))[::-1])))
print(max(gugudan))

