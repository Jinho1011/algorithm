import sys

num = int(sys.stdin.readline())

vote_list = []
count = 0
dasom = 0

for i in range(num):
    vote = int(sys.stdin.readline())
    if i == 0:
        dasom = vote
    else:
        vote_list.append(vote)

if num == 1:
    print(count)
    sys.exit()

vote_list.sort(reverse=True)

while True:
    if dasom <= vote_list[0]:
        vote_list[0] -= 1
        dasom += 1
        count += 1
        vote_list.sort(reverse=True)
    else:
        break

print(count)