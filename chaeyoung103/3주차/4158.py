import sys


while True:
    count = 0
    N, M = map(int, sys.stdin.readline().split())
    if N & M == 0:
        break
    n_set = {int(sys.stdin.readline().strip()) for _ in range(N)}
    m_set = {int(sys.stdin.readline().strip()) for _ in range(M)}

    count = len(n_set & m_set)
    print(count)

