import sys

x1,y1 = map(int, sys.stdin.readline().split())
x2,y2 = map(int, sys.stdin.readline().split())
x3,y3 = map(int, sys.stdin.readline().split())

def compare (a,b,c):
    if a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b

x = compare(x1,x2,x3)
y = compare(y1,y2,y3)

print(x,y)
