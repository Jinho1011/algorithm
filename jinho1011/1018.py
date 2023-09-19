from sys import stdin


def get_fix_cnt(MAP, m, n, init):
    cnt = 0
    NEW_MAP = []

    for i in range(m, m+8):
        line = []
        for j in range(n, n+8):
            line.append(MAP[i][j])
        NEW_MAP.append(line)

    for i in range(0, 8):
        for j in range(0, 8):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                if NEW_MAP[i][j] != init:
                    cnt += 1
            else:
                if NEW_MAP[i][j] == init:
                    cnt += 1

    return cnt


if __name__ == '__main__':
    M, N = (map(int, stdin.readline().split()))
    MAP = []
    cnt_list = []

    for i in range(0, M):
        MAP.append(list(map(str, stdin.readline().strip())))

    for m in range(0, M-7):
        for n in range(0, N-7):
            cnt_list.append(get_fix_cnt(MAP, m, n, 'B'))
            cnt_list.append(get_fix_cnt(MAP, m, n, 'W'))

    print(min(cnt_list))

# 8 8
# WWBWBWBW
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
