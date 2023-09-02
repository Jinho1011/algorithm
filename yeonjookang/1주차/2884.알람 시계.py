H,M = map(int,input().split())

if M>=45: print(f'{H} {M-45}')
else:
    if H<1: print(f'{23+H} {60-(45-M)}')
    else: print(f'{H-1} {60-(45-M)}')
