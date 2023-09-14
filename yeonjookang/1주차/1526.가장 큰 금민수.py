import sys

N = int(sys.stdin.readline())

for i in range(N,0,-1):
    flag=0
    for num in list(str(i)):
        if num=='4' or num=='7':
            continue
        else: flag=1
    if flag==0: 
        print(i)
        exit()

