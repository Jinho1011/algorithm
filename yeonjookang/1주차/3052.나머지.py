last=[]

for _ in range(10):
    n=int(input())
    last.append(n%42)

last=set(last)
print(len(last))