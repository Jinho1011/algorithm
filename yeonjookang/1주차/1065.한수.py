import sys
N=int(sys.stdin.readline())

count=0

for i in range(1,N+1):
    if i < 100: 
        count+=1
        continue
    flag=0
    for j in range(len(str(i))-2):
        if int(list(str(i))[j+1])-int(list(str(i))[j])!=int(list(str(i))[j+2])-int(list(str(i))[j+1]):
            flag=1
    if flag==0: count+=1
print(count)


