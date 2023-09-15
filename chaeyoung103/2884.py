import sys 

h, m = map(int, sys.stdin.readline().split())

if m < 45:
    if h != 0:
        h -= 1
        m = 60 - (45-m)
    else:
        h = 23
        m = 60 - (45-m)
else:
    m = m-45
print(h,m)




