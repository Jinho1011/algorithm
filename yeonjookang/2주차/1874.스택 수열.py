import sys
n=int(sys.stdin.readline())

nums=[i for i in range(n,0,-1)]
input_list=[]

for _ in range(n):
    input_list.append(int(sys.stdin.readline()))

stack=[]
plus_minus=[]

for i in range(n):
    num=input_list[i]
    
    while num not in stack:
        stack.append(nums.pop())
        plus_minus.append('+')
    
    pop_num=stack.pop()
    plus_minus.append('-')
    if pop_num==num:
        continue
    else:
        print('NO')
        sys.exit()

for plus in plus_minus:
    print(plus)


        