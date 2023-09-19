import sys
N=int(sys.stdin.readline())

count = 0
num=str(665)
while 1:
    num=str(int(num)+1)
    
    if '666' in num:
        count+=1
    if count==N:
        print(num)
        break
    