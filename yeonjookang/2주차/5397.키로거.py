import sys

T=int(sys.stdin.readline())

#delete, insert 메서드는 O(N)
#즉, 리스트는 단순 조회할 때만 빠르다

#연결리스트의 insert, delete는 O(N)
#즉, 연결리스트는 조회가 아닌 특정 위치의 원소 삭제 및 추가 시 빠르다

#스택과 큐는 맨 앞, 맨 뒤 원소만 접근 가능하기 때문에 항상 O(1)

for _ in range(T):
    input_str=sys.stdin.readline().strip()
    pos=0
    password=[]
    for input_char in input_str:
        if input_char=='<':
            if pos>0: pos-=1
        elif input_char=='>':
            if pos<len(password): pos+=1
        elif input_char=='-':
            if pos>0: 
                del password[pos-1]
                pos-=1
        else:
            password.insert(pos,input_char)
            pos+=1
    for word in password:
        print(word,end='')
    print()