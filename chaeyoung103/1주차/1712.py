import sys
import math

a, b, c= map(int,sys.stdin.readline().split())

result = -1

if b>=c:
    print(result)
    exit()

result = math.ceil(a / (c-b))

if result*(c-b) == a:
    result += 1

print(result)