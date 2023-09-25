import sys

N, M = map(int, sys.stdin.readline().split())
set_N = set()
set_M = set()

for i in range(N):
    input_N = str(sys.stdin.readline().strip())
    set_N.add(input_N)
for i in range(M):
    input_M = str(sys.stdin.readline().strip())
    set_M.add(input_M)

result = list(set_N & set_M)
result.sort()

print(len(result))
print(str(result).replace('[','').replace(']','').replace(',','').replace("'",'').replace(' ', '\n'))

