year=int(input())
flag=0
if year%4==0:
    if year%400==0:
        flag=1
    else:
        if year%100!=0:
            flag=1
print(flag)
