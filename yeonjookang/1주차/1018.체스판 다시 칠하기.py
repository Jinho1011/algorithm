import sys

#N:행, M:열
N,M=map(int,sys.stdin.readline().split())

chess_start_black=[['W' if i%2==0 else 'B' for i in range(1,9)] if j%2!=0 else ['B' if i%2==0 else 'W' for i in range(1,9)] for j in range(1,9)]
chess_start_white=[['B' if i%2==0 else 'W' for i in range(1,9)] if j%2!=0 else ['W' if i%2==0 else 'B' for i in range(1,9)] for j in range(1,9)]
chess_input=[['A' for _ in range(M)] for _ in range(N)]

answer_compare_white=250
answer_compare_black=250

for i in range(N):
    line=sys.stdin.readline().strip()
    for j in range(M):
        chess_input[i][j]=list(line)[j]

for i in range(0,N-7):
    for j in range(0,M-7):
        count_compare_white=0
        count_compare_black=0
        for s in range(8):
            for t in range(8):
                if chess_input[i+s][j+t]!=chess_start_white[s][t]:
                    count_compare_white+=1
                if chess_input[i+s][j+t]!=chess_start_black[s][t]:
                    count_compare_black+=1
        answer_compare_black=min(answer_compare_black,count_compare_black)
        answer_compare_white=min(answer_compare_white,count_compare_white)

print(min(answer_compare_white,answer_compare_black))


