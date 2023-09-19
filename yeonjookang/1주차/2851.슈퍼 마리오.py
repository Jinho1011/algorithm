import sys

mushrooms=[]

for _ in range(10):
    mushrooms.append(int(sys.stdin.readline()))

score=0
for mushroom in mushrooms:
    score+=mushroom
    if score>=100:
        if score-100<=100-score+mushroom:
            print(score)
            exit()
        else:
            print(score-mushroom)
            exit()
print(sum(mushrooms))