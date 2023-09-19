import sys
X,Y,P_1,P_2=map(int,sys.stdin.readline().split())

x_list=[]
y_list=[]

for i in range(0,1000):
    X_JUMP=P_1+X*i
    Y_JUMP=P_2+Y*i
    x_list.append(X_JUMP)
    y_list.append(Y_JUMP)

    if Y_JUMP in x_list : 
        print(Y_JUMP) 
        exit()
    if X_JUMP in y_list : 
        print(X_JUMP)
        exit()
print(-1)