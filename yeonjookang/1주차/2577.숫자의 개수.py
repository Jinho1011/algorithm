A=int(input())
B=int(input())
C=int(input())

ABC=A*B*C

for i in range(0,10):
    print(str(ABC).count(str(i)))