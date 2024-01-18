import sys

input_str=sys.stdin.readline()
stack=[]
flag=0

for input_char in input_str:
    if input_char=='<':
        if len(stack)!=0:
            print(''.join(stack[::-1]),end='')
            stack.clear()
        stack.append(input_char)
        flag=1
    elif input_char=='>':
        stack.append(input_char)
        print(''.join(stack),end='')
        stack.clear()
        flag=0
    elif input_char==' ' or input_char=='\n':
        if flag!=1:
            print(''.join(stack[::-1]),end='')
            print(' ',end='')
            stack.clear()
        else:
            stack.append(' ')
    else:
        stack.append(input_char)
