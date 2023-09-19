import sys
T = int(sys.stdin.readline())

for _ in range(T):
    input_string=sys.stdin.readline().strip()
    stack=[]
    flag=1
    for str in input_string:
        if str=='(':
            stack.append(str)
        if str==')':
            if len(stack)>0:
                stack.pop()
            else:
                flag=0
                break
    if flag==0 or len(stack)>0:
        print('NO')
    else:
        print('YES')

