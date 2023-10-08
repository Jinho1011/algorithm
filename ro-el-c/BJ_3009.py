import sys
input = sys.stdin.readline

x=[]
y=[]

for _ in range(3):
    tempX, tempY = map(int, input().split())
    
    if tempX not in x:
        x.append(tempX)
    else:
        x.remove(tempX)

    if tempY not in y:
        y.append(tempY)
    else:
        y.remove(tempY)

print(x[0], y[0])

"""
3점 -> 축에 평행한 직사각형을 만들기 위한 네 번째 점
"""