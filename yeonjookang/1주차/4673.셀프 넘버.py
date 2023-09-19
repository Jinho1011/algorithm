nums=[]
for i in range(1,10001):
    nums.append(i)

for i in range(1,10001):
    sum=i
    for n in list(str(i)):
        sum+=int(n)
    if sum in nums:
        nums.remove(sum)
for num in nums:
    print(num)