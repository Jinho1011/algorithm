import sys
n=int(sys.stdin.readline())

# nums=[i for i in range(n,0,-1)]
# input_list=[]

# for _ in range(n):
#     input_list.append(int(sys.stdin.readline()))

# stack=[]
# plus_minus=[]

# for i in range(n):
#     num=input_list[i]
    
#     while num not in stack:
#         stack.append(nums.pop())
#         plus_minus.append('+')
    
#     pop_num=stack.pop()
#     plus_minus.append('-')
#     if pop_num==num:
#         continue
#     else:
#         print('NO')
#         sys.exit()

# for plus in plus_minus:
#     print(plus)

stack=[]
escalate_nums=[i for i in range(n,0,-1)]
plus_minus_result=[]

def top(stack):
    if len(stack)==0:
        return 0
    else:
        stack_top=stack.pop()
        stack.append(stack_top)
        return stack_top

for i in range(n):
    input_num=int(sys.stdin.readline())
 
    #들어온 수랑 top이랑 비교 후 같아질 때까지 push 또는 pop 진행
    stack_top=top(stack)
    while(stack_top!=input_num):
        if stack_top<input_num:
            #더이상 스택에 넣을 오름차순이 없을 때
            if len(escalate_nums)==0:
                print('NO')
                sys.exit()
            stack.append(escalate_nums.pop())
            plus_minus_result.append('+')
        elif stack_top>input_num:
            #더이상 스택에 아무것도 없을 때
            if len(stack)==0:
                print('NO')
                sys.exit()
            stack.pop()
            plus_minus_result.append('-')
        stack_top=top(stack)

    #같아지면 pop
    if stack_top==input_num:
        stack.pop()
        plus_minus_result.append('-')

for i in plus_minus_result:
    print(i)