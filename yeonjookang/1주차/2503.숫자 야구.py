import sys
N=int(sys.stdin.readline())

nums=[]
invalid_nums = []

for i in range(100,1000):
    flag=0
    for j in range(10):
        if str(i).count(str(j))>1:
            flag=1
            break
    if flag==0: nums.append(i)

for _ in range(N):
    M,S,B=map(int,sys.stdin.readline().split())
    for num in nums:
        S_count=0
        B_count=0
        for i in range(3):
            if list(str(num))[i]==list(str(M))[i]:
                S_count+=1
            elif list(str(M)).count(list(str(num))[i])>0:
                B_count+=1
        if S_count!=S or B_count!=B:
            invalid_nums.append(num)
    for num in invalid_nums:
        if num in nums: nums.remove(num)
print(len(nums))
