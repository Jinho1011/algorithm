import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
input_nums=list(map(int,sys.stdin.readline().split()))

nums_deque=deque()

for i in range(1,N+1):
    nums_deque.append(i)

answer_cnt=0

while len(input_nums)!=0:
    # 1번 수행 가능 경우
    if input_nums[0]==nums_deque[0]:
        input_nums.remove(input_nums[0])
        nums_deque.popleft()
        continue
    # 2,3번 수행 경우
    else:
        # 해당 숫자 위치 찾기
        num_spot=0
        index=0
        while 1:
            if nums_deque[index]==input_nums[0]:
                num_spot=index
                break
            else: index+=1
        # 3번 수행 경우
        if num_spot>len(nums_deque)//2:
            cnt=0
            while nums_deque[0]!=input_nums[0]:
                nums_deque.appendleft(nums_deque.pop())
                cnt+=1
            input_nums.remove(input_nums[0])
            nums_deque.popleft()
            answer_cnt+=cnt
        # 2번 수행 경우
        else:
            cnt=0
            while nums_deque[0]!=input_nums[0]:
                nums_deque.append(nums_deque.popleft())
                cnt+=1
            input_nums.remove(input_nums[0])
            nums_deque.popleft()
            answer_cnt+=cnt
print(answer_cnt)