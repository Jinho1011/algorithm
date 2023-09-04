nums = []

for i in range(1,11):
    nums.append(int(input()) % 42)

print(len(set(nums)))