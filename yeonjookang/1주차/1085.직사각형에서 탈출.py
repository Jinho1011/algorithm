x,y,w,h=map(int,input().split())

distance=[x,y,w-x,h-y]

print(min(distance))