import sys

N=int(sys.stdin.readline())
input_str=list(sys.stdin.readline().strip())

operand=[]
for _ in range(N):
    operand.append(int(sys.stdin.readline()))

cnt=0
for input_char in input_str:
    if input_char!='+' and input_char!='-' and input_char!='*' and input_char!='/' :
        input_str[cnt]=str(operand[ord(input_char)-ord('A')])
    cnt+=1

calculation=[]

for input_char in input_str:
    if input_char=='+':
        a=calculation.pop()
        b=calculation.pop()
        calculation.append(a+b)
    elif input_char=='-':
        a=calculation.pop()
        b=calculation.pop()
        calculation.append(b-a)
    elif input_char=='*':
        a=calculation.pop()
        b=calculation.pop()
        calculation.append(a*b)
    elif input_char=='/':
        a=calculation.pop()
        b=calculation.pop()
        calculation.append(b/a)
    else: calculation.append(int(input_char))

print("{:.2f}".format(calculation[0]))
