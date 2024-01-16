import sys
T=int(sys.stdin.readline())
for _ in range(T):
    input_str=sys.stdin.readline()
    stack=[]
    for one_char in input_str:
        if(one_char==" " or one_char=="\n"):
            for _ in range(len(stack)):
                print(stack.pop(),end='')
            print(end=" ")
        else:
            stack.append(one_char)
    print()
        