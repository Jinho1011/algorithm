a, b, c = list(map(int, input().split()))

print(int(a / (c - b)) + 1) if c > b else print(-1)

