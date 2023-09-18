import sys

result_list = []

while True:
    x, y, z = map(int, sys.stdin.readline().split())

    if x != 0:
        max_side = max(x,y,z)
        if (max_side**2)*2 == x**2 + y**2 + z**2:
            result_list.append('right')
        else:
            result_list.append('wrong')
    else:
        break

for i in result_list:
    print(i)