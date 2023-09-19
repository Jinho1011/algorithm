import sys

def solution(n, k):
    arr = [i for i in range(1,n+1)]
    res = []
    idx = 0

    for i in range(n):
        idx += k-1
        if idx >= len(arr):
            idx %= len(arr)

        res.append(str(arr[idx]))    
        arr.pop(idx)

    return res


if __name__ == "__main__":
    # N, K = 7, 3
    N, K = map(int, sys.stdin.readline().split())

    answer = solution(N, K)
    print("<",", ".join(list(map(str, answer)))[:],">", sep='')