# 전자레인지

import sys
input = sys.stdin.readline

T = int(input())

if T % 10 != 0: # 3개의 버튼으로 정학히 맞출 수 없는 경우
    print(-1)
    sys.exit()

a, b, c = 300, 60, 10
clickA, clickB, clickC = 0, 0, 0

while T > 0:
    clickA += T // a
    T %= a

    clickB += T // b
    T %= b

    clickC += T // c
    T %= c

print(clickA, clickB, clickC)

"""
시간 조절용 버튼 a 300s / b 60s / c 10s
냉동음식 요리 시간 T(s)
-> 최소 버튼 조작
+) 정확히 맞출 수 없는 경우 -1 반환


그리디(Greedy) - 거스름돈 문제

1. 1의 자리 숫자가 0이 아닌 경우를 제외하면,
   모두 a/b/c 세 버튼으로 시간을 정확히 맞출 수 있다.
2. a, b, c 버튼 순서로 가능한 횟수를 정해야 한다.
   (남은 시간의 절감을 크게 하기 위함)

-> 가지고 있는 버튼의 큰 단위가 항상 작은 단위의 배수이므로, 그리디 알고리즘을 사용하여 최적해를 도출할 수 있음

"""