from itertools import combinations

x_list=[]
y_list=[]

for _ in range(3):
    x,y=map(int,input().split())
    
    x_list.append(x)
    y_list.append(y)

#직사각형의 각 점을 조사하면
#각각 x_list와 y_list에는 10,10,30,30 같이 중복되는 수가 2개씩 4개가 있어야 한다. 

for x in combinations(x_list,2):
    if x[0]==x[1]:
        #x는 나머지 하나
        x_list.remove(x[0])
        x_list.remove(x[1])
x=x_list[0]

for y in combinations(y_list,2):
    if y[0]==y[1]:
        #y는 나머지 하나
        y_list.remove(y[0])
        y_list.remove(y[1])
y=y_list[0]

print(f'{x} {y}')