import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1, n + 1):
    tmp = str(i)
    cnt += tmp.count('3') + tmp.count('6') + tmp.count('9')

print(cnt)