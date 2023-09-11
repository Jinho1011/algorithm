import sys
import math
input = sys.stdin.readline

while True:
    b, n = map(int, input().split())
    if b == 0 and b == 0:
        break

    tmp = b ** (1 / n)
    up = math.ceil(tmp)
    down = math.floor(tmp)

    print(down if (abs(b-up**n) > abs(b-down**n)) else up)
