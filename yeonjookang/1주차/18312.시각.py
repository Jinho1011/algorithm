import sys

N,K=map(int,sys.stdin.readline().split())

time_분=[]
time_초=[]
answer=0

for i in range(0,60):
    time_분.append(i)
    time_초.append(i)

for i in range(0,N+1):
    if i<10: str_i='0'+str(i)
    else: str_i=str(i)
    for 분 in time_분:
        for 초 in time_초:
            if 분<10: str_분='0'+str(분)
            else: str_분=str(분)
            if 초<10: str_초='0'+str(초)
            else: str_초=str(초)

            if str_i.count(str(K))>0 or str_분.count(str(K))>0 or str_초.count(str(K))>0 :
                answer+=1
print(answer)