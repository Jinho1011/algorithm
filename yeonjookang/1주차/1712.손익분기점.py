A,B,C=map(int,input().split())

if C-B<=0:
    print(-1)
else:
    # 반복문을 쓰지 말기!
    # i=1
    # while 1:
    #     if A+B*i<C*i:
    #         print(i)
    #         break
    #     i+=1
    print(int(A/(C-B)+1))
