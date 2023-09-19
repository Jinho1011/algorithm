import sys

num = int(sys.stdin.readline())


for i in range(num):
    count1 = 0
    count2 = 0
    a = list(str(sys.stdin.readline()))
    for j in a:
        if j == '(':
            count1 += 1
        elif j == ')':
            count2 += 1
        if count1 < count2:
            break
    if count1 != count2:
        print('NO')
    else:
        print('YES')


