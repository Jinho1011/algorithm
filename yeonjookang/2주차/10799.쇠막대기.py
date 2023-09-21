import sys

input_str=sys.stdin.readline().strip()

stack=[]
cnt=0

for i in range(0,len(input_str)):
    if i==0: pre_input=''
    else: pre_input=input_str[i-1]

    if input_str[i]=='(':
        stack.append('(')
    else:
        #레이저인 경우
        if pre_input=='(':
            stack.pop()
            cnt+=len(stack)
        #쇠막대기인 경우
        else:
            cnt+=1
            stack.pop()

print(cnt)


    


