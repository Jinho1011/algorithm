from sys import stdin


if __name__ == '__main__':
    N = int(stdin.readline())
    devils = []
    index = 666

    while True:
        if len(devils) == N:
            break
        str_index = str(index)
        if str_index.find('666') > -1:
            devils.append(index)
        index += 1

    print(devils.pop())
