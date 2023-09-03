import sys
from itertools import combinations

while 1:
    a,b,c=map(int,input().split())
    lengths=[a,b,c]
    if a==b==c==0:
        sys.exit()
    max_length=max(lengths)
    lengths.remove(max_length)
    if max_length**2==lengths[0]**2+lengths[1]**2:
        print("right")
    else: print("wrong")

