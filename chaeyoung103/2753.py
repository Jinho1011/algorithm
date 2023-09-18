import sys

year = int(sys.stdin.readline().strip())
result = 0

if (year%4) == 0:
    if (year%100) != 0:
        result = 1
    else:
        if (year%400)==0:
            result = 1

print(result)