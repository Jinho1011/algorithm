import sys

N=int(sys.stdin.readline())
remain_list=[]

for _ in range(N):
    name,log=map(str,sys.stdin.readline().split())
    if log=='enter': remain_list.append(name)
    else : remain_list.remove(name)
remain_list.sort(reverse=True)

for remain in remain_list:
    print(remain)