n=int(input())
count=0

for i in range(1,n+1):
    count+=str(i).count(str(3))
    count+=str(i).count(str(6))
    count+=str(i).count(str(9))
    
print(count)