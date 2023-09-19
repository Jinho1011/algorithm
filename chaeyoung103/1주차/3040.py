import sys
num_list = []
sum = 0
rest = 0

for i in range(9):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)
    sum += num
    rest = sum - 100

for n in num_list:
    for k in num_list:
        if (n != k) & ((n+k) == rest):
            num_list.remove(n)
            num_list.remove(k)
            break

for n in num_list:
    print(n)