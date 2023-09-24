import sys

T=int(sys.stdin.readline())

#delete, insert 메서드는 O(N)
#즉, 리스트는 단순 조회할 때만 빠르다

#스택과 큐는 맨 앞, 맨 뒤 원소만 접근 가능하기 때문에 항상 O(1)


for _ in range(T):
    input_str=sys.stdin.readline().strip()
    password=[]
    sub=[]
    for input_char in input_str:
        if input_char == '<':
            if len(password)!=0:
                sub.append(password.pop())
        elif input_char == '>':
            if len(sub)!=0:
                password.append(sub.pop())
        elif input_char == '-':
            if len(password)!=0:
                password.pop()
        else:
            password.append(input_char)
    print("".join(password),"".join(sub[::-1]),sep="")        
