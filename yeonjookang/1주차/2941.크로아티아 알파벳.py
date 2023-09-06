import sys
S=sys.stdin.readline().rstrip()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

num=0
for i in range(len(croatia)):
    if croatia[i] in S:
        num+=S.count(croatia[i])
        S=S.replace(croatia[i],'0')
for s in S:
    if s!='0' :num+=1
print(num)