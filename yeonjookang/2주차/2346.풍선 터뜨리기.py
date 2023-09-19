import sys
N=int(sys.stdin.readline())

balloon_list=list(map(int,sys.stdin.readline().split()))
answer_list=[1]

move=0
index=0

for i in range(N):
    cnt=0
    if i==0:
        move=balloon_list[i]
        balloon_list[i]=0
    else:
        if move>0:
            while cnt!=move:
                index+=1
                if index>=len(balloon_list): index=0
                if balloon_list[index]!=0:
                    cnt+=1
            move=balloon_list[index]
            balloon_list[index]=0
            answer_list.append(index+1)
        else:
            while cnt!=move:
                index-=1
                if index<0: index=len(balloon_list)-1
                if balloon_list[index]!=0:
                    cnt-=1
            move=balloon_list[index]
            balloon_list[index]=0
            answer_list.append(index+1)  

for answer in answer_list:
    print(answer,end=' ')

