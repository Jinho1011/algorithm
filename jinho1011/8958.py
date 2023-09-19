cnt = int(input())

for i in range(cnt):
    tc = input()
    res = 0
    num = 0
    for j in range(len(tc)):
        if tc[j] == 'O':
            num += 1
        else:
            num = 0
        res += num

    print(res)