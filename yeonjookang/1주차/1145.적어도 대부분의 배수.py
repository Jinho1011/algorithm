import sys

nums = list(map(int,sys.stdin.readline().split()))

i=1
while 1:
    count=0
    for num in nums:
        if i%num==0: count+=1
    if count >2:
        print(i)
        break
    i+=1
