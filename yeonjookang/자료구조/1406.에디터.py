import sys

input_str=sys.stdin.readline().strip()

# 문자열->리스트(list), 리스트->문자열(join 함수)
stack_left=list(input_str)
stack_right=[]

M=int(sys.stdin.readline())

for _ in range(M):
    input_cmd=sys.stdin.readline().strip()
    list_cmd=input_cmd.split(' ')
    cmd=list_cmd[0]
    if cmd=='L':
        if len(stack_left)!=0:
            stack_right.append(stack_left.pop())
    if cmd=='D':
        if len(stack_right)!=0:
            stack_left.append(stack_right.pop())
    if cmd=='B':
        if len(stack_left)!=0:
            stack_left.pop()
    if cmd=='P':
        stack_left.append(list_cmd[1])

print(''.join(stack_left)+''.join(stack_right[::-1]))