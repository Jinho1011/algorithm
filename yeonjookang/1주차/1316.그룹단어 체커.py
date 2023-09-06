import sys
N = int(sys.stdin.readline())
num=0 

for i in range(N):
    S = sys.stdin.readline().rstrip()
    list_alphabet = []
    
    flag=0
    # 리스트에 문자가 없으면 저장
    # 바로 전 문자와 같으면 패스 (첫번째 문자는 not in에 무조건 걸리므로 고려할 필요 X)
    # 리스트에 문자가 있는데 새로운 문자면 그룹 단어가 아님

    for j in range(len(S)):
        if S[j] not in list_alphabet: 
            list_alphabet.append(S[j])
            continue
        if S[j] == S[j-1] : continue   
        else : flag=1
    
    if flag != 1 : num+=1

print(num)
        

   
