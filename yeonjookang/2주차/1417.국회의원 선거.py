import sys
N=int(sys.stdin.readline())
vote_list=[]

dasom=int(sys.stdin.readline())

for _ in range(N-1):
    vote_list.append(int(sys.stdin.readline()))
vote_list.sort(reverse=True)
answer=0

if N==1:
    print(answer)
    sys.exit()

while 1:
    for i in range(0,N-1):
        if dasom<=vote_list[i]:
            dasom+=1
            vote_list[i]-=1
            answer+=1
            vote_list.sort(reverse=True)
            break
        elif i==N-2:
            print(answer)
            sys.exit()



