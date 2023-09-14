X, Y, p1, p2 = list(map(int, input().split()))

l1 = []
l2 = []
i = 0
found = False

while i<1000:
    if X*i + p1 in l2:
        print(X*i + p1)
        found = True
        break

    if Y*i + p2 in l1:
        print(Y*i + p2)
        found = True
        break

    l1.append(X*i + p1)
    l2.append(Y*i + p2)
    i += 1
        
if found is False:
    print(-1)
