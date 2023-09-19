n=int(input())
for _ in range(n):
    H,W,N=map(int,input().split())
    x=N%H
    y=int(N//H)+1
    
    if(x==0): 
        x=H
        y=y-1

   

    if(y<10): print(f'{x}0{y}')
    else: print(f'{x}{y}')

    