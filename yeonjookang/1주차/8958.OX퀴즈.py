n=int(input())
for _ in range(n):
    string=input()
    answer=0
    num=0
    for c in string:
        if(c=='O'):
            num+=1
            answer+=num
        else:
            num=0
    print(answer)