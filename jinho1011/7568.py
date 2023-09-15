n = int(input())

ranks = []

for i in range(n):
    x, y = list(map(int, input().split()))
            
    ranks.append((x,y))


for i in ranks:
    rank = 1
    for j in ranks:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, "")
    
