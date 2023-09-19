N = int(input())
print(sum(str(i).count('3') + str(i).count('6') + str(i).count('9') if '3' in str(i) or '6' in str(i) or '9' in str(i) else 0 for i in range(1, N + 1)))
