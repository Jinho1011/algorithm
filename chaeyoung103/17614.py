import sys
num = int(sys.stdin.readline().strip())

count = 0
for i in range(num):
    result = str(i+1)
    if result.count('3') > 0 or result.count('6')>0 or result.count('9')>0:
        count += result.count('3') + result.count('6') + result.count('9')

print(count)