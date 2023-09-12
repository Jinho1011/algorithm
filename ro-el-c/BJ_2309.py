import sys
input = sys.stdin.readline

height = []
sum  = 0
for _ in range(9):
    tmp = int(input())
    height.append(tmp)
    sum += tmp

for i in range(len(height)-1):
    for j in range(i+1, len(height)):
        if sum - height[i] - height[j] == 100:
            height.remove(height[j])
            height.remove(height[i])
            height.sort()
            for i in height:
                print(i)
            sys.exit()