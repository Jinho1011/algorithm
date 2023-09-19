import sys
N=int(sys.stdin.readline())

cnt=0
for _ in range(N):
    stack=[]
    word=sys.stdin.readline().strip()
    for a_or_b in word:
        if len(stack)!=0 and a_or_b==stack[len(stack)-1]:
            stack.pop()
            continue
        else: stack.append(a_or_b)
    if len(stack)==0:
        cnt+=1
print(cnt)